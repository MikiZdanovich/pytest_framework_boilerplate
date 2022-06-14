class ValidationErrors:

    @staticmethod
    def invalid_status_code(status_code, expected_status_code):
        return 'Invalid status code: {0} instead of {1}'.format(status_code, expected_status_code)
