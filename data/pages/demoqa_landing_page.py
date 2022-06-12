from data.locators.demoqa_landing_page import SetLandingPageLocators
from src.base.base_page import WebPage
from src.base.base_element import WebElement


class LandingPage(WebPage):
    """This is sample test page"""

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def welcome_heading(self):
        return WebElement(SetLandingPageLocators.header_locator)
