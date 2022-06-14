from src.exceptions.validation_errors import ValidationErrors


class BaseResponse:
    def __int__(self, response):
        self.response = response
        self.response_status_code = self.response.status_code
        self.response_json = self.response.json()
        self.response_data = self.response_json.get('data')
        self.response_metadata= self.response_json.get('metadata')

    def validate_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status_code in status_code, ValidationErrors.invalid_status_code(
                self.response_status_code, status_code)
        else:

            assert self.response_status_code == status_code, ValidationErrors.invalid_status_code(
                self.response_status_code, status_code)

        return self

    def validate_response_schema(self, schema):
        if isinstance(self.response_json, list):
            for response_item in self.response_json:
                schema.parse_obj(response_item)
        else:
            schema.parse_obj(self.response_json)

        return self
