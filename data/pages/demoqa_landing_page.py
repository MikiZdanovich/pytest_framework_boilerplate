from data.locators.demoqa_landing_page import LandingPageLocators
from src.base.ui.base_page import WebPage
from src.base.ui.base_element import WebElement


class LandingPage(WebPage):
    """This is sample test page"""

    def __init__(self, driver):
        super().__init__(driver)

    @property
    def welcome_heading(self):
        return WebElement(LandingPageLocators.header_locator)

    def get_welcome_heading_text(self):
        return self.welcome_heading.get_text()