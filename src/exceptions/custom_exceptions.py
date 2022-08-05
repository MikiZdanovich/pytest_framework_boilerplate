class EnvironmentVariableException(Exception):
    """ This class is used to raise an exception when the environment variable is not set. """

    def __init__(self, variable_key):
        self.variable_key = variable_key
        self.message = f'Environment variable {variable_key} is not set!'
        super().__init__(self.message)


class UnsupportedBrowserException(Exception):
    """Exception raised for unsupported browsers.

       Attributes:
           browser -- browser name
           supported_browsers -- list of supported browsers
       """

    def __init__(self, browser, supported_browsers):
        self.browser = browser
        self.supported_browsers = supported_browsers
        self.message = f'{browser} is not in list supported browsers : {supported_browsers}'
        super().__init__(self.message)
