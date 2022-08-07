from src.enums.validation_errors_enum import ValidationErrorMessage


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
