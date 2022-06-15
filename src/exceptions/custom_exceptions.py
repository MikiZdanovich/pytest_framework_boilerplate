

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

    def __str__(self):
        return self.message
