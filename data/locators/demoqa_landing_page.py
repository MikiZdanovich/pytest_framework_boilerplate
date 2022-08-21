from dataclasses import dataclass
from src.base.ui.locator import BaseLocator
from selenium.webdriver.common.by import By


@dataclass
class LandingPageLocators(BaseLocator):
    """
    Locators for LandingPage.
    """

    header_locator: tuple[By, str] = (By.CLASS_NAME, 'heading')
