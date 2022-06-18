from enum import Enum


class ValidationErrorMessage(Enum):
    MissingData = 'Data object is missing'
    MissingMetadata = 'Metadata object is missing'
    InvalidStatusCode = 'Invalid status code: {0} instead of {1}'


class ValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class StatusCodeException(Exception):
    def __init__(self, actual, expected):
        self.actual = actual
        self.expected = expected
        self.message = ValidationErrorMessage.InvalidStatusCode.value.format(actual, expected)
        super().__init__(self.message)
