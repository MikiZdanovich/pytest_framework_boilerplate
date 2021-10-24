from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from msedge.selenium_tools import EdgeOptions, Edge


class DriverFactory:

    @staticmethod
    def get_driver(browser, headless_mode=False):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            if headless_mode is True:
                options.add_argument("--headless")

            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            return driver

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless_mode is True:
                options.headless = True
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
            return driver

        elif browser == "edge":
            options = EdgeOptions()
            options.use_chromium = True
            if headless_mode is True:
                options.headless = True
            driver_path = EdgeChromiumDriverManager().install()
            driver = Edge(executable_path=driver_path, options=options)
            return driver

        raise Exception("Provide valid driver name")
