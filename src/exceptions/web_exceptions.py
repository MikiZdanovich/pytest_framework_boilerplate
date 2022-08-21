from src.enums.ui_errors_enum import UiErrorMessages


class FailedToGetPageSourceException(Exception):
    def __init__(self):
        self.message = UiErrorMessages.PageSourceNotFound.value
        super().__init__(self.message)


class WebElementNotFoundException(Exception):
    def __init__(self, element_locator):
        self.message = UiErrorMessages.WebElementNotFound.value.format(element_locator)
        super().__init__(self.message)


class NotEnoughTimeToLocateElementException(Exception):
    def __init__(self, element_locator, timeout):
        self.message = UiErrorMessages.TimeToLocateElementExceedMessage.value.format(element_locator, timeout)
        super().__init__(self.message)


class PageTookTooLongToResponseException(Exception):
    def __init__(self, url, timeout):
        self.message = UiErrorMessages.TimeToLocateElementExceedMessage.value.format(url, timeout)
        super().__init__(self.message)