from json import JSONDecodeError

from src.exceptions.validation_errors import ValidationError, ValidationErrorMessage, StatusCodeException


class BaseResponse:
    def __init__(self, response):
        self.response = response
        self.response_status_code = self.response.status_code
        self.response_json = self.get_json()

    def _get_response_data(self):
        try:
            if isinstance(self.response_json, dict):
                return self.response_json['data']
            else:
                return [obj['data'] for obj in self.response_json]
        except KeyError:
            raise ValidationError(ValidationErrorMessage.MissingData.value)

    def _get_response_metadata(self):
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

    def get_json(self):
        try:
            json = self.response.json()
        except JSONDecodeError:
            json = {}
