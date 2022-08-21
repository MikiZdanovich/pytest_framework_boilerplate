from src.base.enum.base_enum import BaseEnum


class UiErrorMessages(BaseEnum):
    PageSourceNotFound = 'Failed to get page source'
    WebElementNotFound = 'Element with locator {0} not found'
    TimeToLocateElementExceedMessage = 'Time exceed to locate element with locator {0} in {1} seconds'
    TimeToLoadPageExceedMessage = 'Time exceed to load page {0} in {1} seconds, time exceeded'
