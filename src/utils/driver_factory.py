from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.remote.webdriver import BaseWebDriver
from selenium.webdriver.common.options import ArgOptions


from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from src.exceptions.custom_exceptions import UnsupportedBrowserException
from src.utils.driver_config_parser import Config as DriverConfig
from src.enums.supported_browsers_enum import SupportedBrowsers


class DriverFactory:
    SUPPORTED_BROWSERS = SupportedBrowsers.get_list()

    @staticmethod
    def set_driver_options(browser: str, options: ArgOptions) -> None:
        browser_config = DriverConfig.set_config(browser)
        for option in browser_config:
            options.add_argument(option)

    @staticmethod
    def _setup_driver(browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            _driver = webdriver.Chrome
            service = ChromeService(ChromeDriverManager().install())

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            _driver = webdriver.Firefox
            service = FirefoxService(GeckoDriverManager().install())

        else:
            raise UnsupportedBrowserException(browser, DriverFactory.SUPPORTED_BROWSERS)

        return options, _driver, service

    @staticmethod
    def get_driver(browser: str) -> BaseWebDriver:

        options, _driver, service = DriverFactory._setup_driver(browser)

        DriverFactory.set_driver_options(browser, options)

        driver = _driver(service=service, options=options)

        driver.implicitly_wait(DriverConfig.set_implicity_wait_time())
        driver.set_page_load_timeout(DriverConfig.set_page_load_timeout())

        if 'headless' in DriverConfig.set_config(browser):
            driver.maximize_window()

        return driver
