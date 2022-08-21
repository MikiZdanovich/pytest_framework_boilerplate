from data.locators.demoqa_landing_page import LandingPageLocators
from src.base.ui.base_page import WebPage
from src.base.ui.locator import BaseLocator
from selenium.webdriver.remote.webdriver import WebDriver


class LandingPage(WebPage):
    """This is sample test page"""

    def __init__(self, driver: WebDriver, locators: BaseLocator() = LandingPageLocators):
        super().__init__(driver)
        self.locators = locators()

    @property
    def heading_text(self) -> str:
        current_heading_text = self.find_element(*self.locators.header_locator).text
        return current_heading_text
