from json import JSONDecodeError

import pydantic
import requests

from src.exceptions.validation_errors import ValidationError, ValidationErrorMessage, StatusCodeException


class BaseResponse:
    def __init__(self, response: requests.Response):
        self.parsed_response = None
        self.response = response
        self.response_status_code = self.response.status_code

    @property
    def response_json(self):
        try:
            _json = self.response.json()
        except JSONDecodeError:
            _json = None
        return _json

    @property
    def response_data(self):
        try:
            if isinstance(self.response_json, dict):
                return self.response_json['data']
            else:
                return [obj['data'] for obj in self.response_json]
        except KeyError:
            raise ValidationError(ValidationErrorMessage.MissingData.value)

    @property
    def response_metadata(self):
        try:
            if isinstance(self.response_json, dict):
                return self.response_json['metadata']
            else:
                return [obj['metadata'] for obj in self.response_json]
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
        temp = self.response_json

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
        if isinstance(self.response_json, list):
            for obj in self.response_json:
                self._validate_json_response(keys, actual_value, obj)
        else:
            self._validate_json_response(keys, actual_value)

    def validate_schema(self, schema: pydantic.BaseModel):
        if isinstance(self.response_json, list):
            self.parsed_response = []
            for obj in self.response_json:
                self.parsed_response.append(schema.parse_obj(obj))
        else:
            self.parsed_response = schema.parse_obj(self.response_json)
        return self
