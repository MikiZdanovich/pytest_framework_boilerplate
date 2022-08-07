from src.base.enum.base_enum import BaseEnum


class ValidationErrorMessage(BaseEnum):
    MissingData = 'Data object is missing'
    MissingMetadata = 'Metadata object is missing'
    InvalidStatusCode = 'Invalid status code: {0} instead of {1}'
