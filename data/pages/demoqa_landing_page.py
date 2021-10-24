import os

from selenium.webdriver.common.by import By

from src.base.base_page import WebPage
from src.base.base_element import WebElement
from src.utils.locator import Locator


class LandingPage(WebPage):
    """This is sample test page"""
    def __init__(self, driver, url=""):

        if not url:
            url = os.getenv('MAIN_URL')

        super().__init__(driver, url)

    @property
    def welcome_heading(self):
        header_locator = Locator(By.CLASS_NAME, 'heading')
        return WebElement(header_locator)
