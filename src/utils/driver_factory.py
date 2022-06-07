from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from src.utils.custom_exceptions import UnsupportedBrowserException
from src.configs.driver_config import Config as DriverConfig


class DriverFactory:
    SUPPORTED_BROWSERS = ["chrome", "firefox"]

    @staticmethod
    def set_driver_options(browser, options):
        browser_config = DriverConfig(browser).browser_config
        for opt in browser_config:
            options.add_argument(opt)

    @staticmethod
    def get_driver(browser, headless_mode=False):

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            _driver = webdriver.Chrome
            service = ChromeService(ChromeDriverManager().install())

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()

            if headless_mode is True:
                options.headless = True
            _driver = webdriver.Firefox
            service = FirefoxService(GeckoDriverManager().install())

        else:
            raise UnsupportedBrowserException(browser)

        DriverFactory.set_driver_options(browser, options)

        driver = _driver(service=service, options=options)

        driver.implicitly_wait(DriverConfig(browser).get_implicity_wait_time())

        return driver
