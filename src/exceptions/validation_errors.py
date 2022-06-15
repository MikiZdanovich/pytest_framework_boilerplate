from enum import Enum


class ValidationErrorMessage(Enum):
    MissingData = 'Data object is missing'
    MissingMetadata = 'Metadata object is missing'
    InvalidStatusCode = 'Invalid status code: {0} instead of {1}'


class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    @staticmethod
    def invalid_status_code(status_code, expected_status_code):
        return ValidationErrorMessage.InvalidStatusCode.value.format(status_code, expected_status_code)
