from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from src.utils.custom_exceptions import UnsupportedBrowserException


class DriverFactory:
    SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]

    @staticmethod
    def get_driver(browser, headless_mode=True):

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")

            if headless_mode is True:
                options.add_argument("headless")
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
            return driver

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless_mode is True:
                options.headless = True
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
            return driver

        elif browser == "edge":
            options = webdriver.EdgeOptions()
            if headless_mode is True:
                options.headless = True
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=options)
            return driver

        raise UnsupportedBrowserException(browser, DriverFactory.SUPPORTED_BROWSERS)
