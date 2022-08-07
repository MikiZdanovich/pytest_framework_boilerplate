import json
from json import JSONDecodeError

import pydantic
import requests

from src.exceptions.validation_errors import ValidationError, ValidationErrorMessage, StatusCodeException


class BaseResponse:
    def __init__(self, response: requests.Response):
        self.parsed_response = None
        self._response_json = None
        self.response_metadata = None
        self.response_data = None
        self.response = response
        self.response_status_code = self.response.status_code

    def get_response_json(self):
        try:
            json = self.response.json()
        except JSONDecodeError:
            json = None
        return json

    def get_response_data(self):
        try:
            if isinstance(self._response_json, dict):
                return self._response_json['data']
            else:
                return [obj['data'] for obj in self._response_json]
        except KeyError:
            raise ValidationError(ValidationErrorMessage.MissingData.value)

    def get_response_metadata(self):
        try:
            if isinstance(self._response_json, dict):
                return self._response_json['metadata']
            else:
                return [obj['metadata'] for obj in self._response_json]
        except KeyError:
            raise ValidationError(ValidationErrorMessage.MissingMetadata.value)

    def validate_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, StatusCodeException(
                self.response_status_code, status_code)
        else:

            assert self.response_status_code == status_code, StatusCodeException(
                self.response_status_code, status_code)

        return self

    def _validate_json_response(self, keys, actual_value, response_json=None):
        if response_json:
            temp = response_json
        temp = self._response_json

        try:
            if isinstance(keys, (list, tuple)):
                for key in keys:
                    temp = temp[key]
                    if isinstance(temp, list):
                        temp = temp[0]
            else:
                temp = temp[keys]
        except KeyError:
            raise ValidationError(ValidationErrorMessage.MissingData.value)

        assert temp == actual_value

    def validate_json_response_body_field(self, keys, actual_value):
        if isinstance(self._response_json, list):
            for obj in self._response_json:
                self._validate_json_response(keys, actual_value, obj)
        else:
            self._validate_json_response(keys, actual_value)

    def validate_schema(self, Schema: pydantic.BaseModel):
        if isinstance(self._response_json, list):
            self.parsed_response = []
            for obj in self._response_json:
                self.parsed_response.append(Schema.parse_obj(obj))
        else:
            self.parsed_response = Schema.parse_obj(self._response_json)
        return self
