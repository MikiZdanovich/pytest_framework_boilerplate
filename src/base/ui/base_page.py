from abc import ABC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from src.utils.url_parser import set_url

from src.exceptions.web_exceptions import PageTookTooLongToResponseException, WebElementNotFoundException, \
    NotEnoughTimeToLocateElementException
from selenium.common import StaleElementReferenceException, NoSuchElementException, TimeoutException


class BasePage(ABC):
    """
    Base class for all pages.
    """


class WebPage(BasePage):
    def __init__(self, driver: WebDriver, url: str = None):
        self._web_driver = driver
        self._url = set_url(url)

    def open(self) -> BasePage:
        self._web_driver.get(self._url)
        self.wait_page_loaded()
        return self

    def go_back(self):
        self._web_driver.back()
        self.wait_page_loaded()

    def refresh(self):
        self._web_driver.refresh()
        self.wait_page_loaded()

    def find_element(self, *locator):
        """ Find element on the page. """

        element = None

        try:
            element = self._web_driver.find_element(*locator)
        except (StaleElementReferenceException, NoSuchElementException):
            raise WebElementNotFoundException(locator)

        return element

    def wait_element(self, *locator, timeout: int = 10) -> None:
        try:
            WebDriverWait(self._web_driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise NotEnoughTimeToLocateElementException(locator, timeout)

    def screenshot(self, file_name: str = 'screenshot.png'):
        self._web_driver.save_screenshot(file_name)

    def scroll_down(self, offset: int = None):
        """ Scroll the page down. """

        if offset:
            self._web_driver.execute_script('window.scrollTo(0, {0});'.format(offset))
        else:
            self._web_driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    def scroll_up(self, offset: int = None) -> None:
        """ Scroll the page up. """

        if offset:
            self._web_driver.execute_script('window.scrollTo(0, -{0});'.format(offset))
        else:
            self._web_driver.execute_script('window.scrollTo(0, -document.body.scrollHeight);')

    def switch_to_iframe(self, iframe: str) -> None:
        """ Switch to iframe by it's name. """

        self._web_driver.switch_to.frame(iframe)

    def switch_out_iframe(self) -> None:
        """ Cancel iframe focus. """
        self._web_driver.switch_to.default_content()

    def get_current_url(self) -> str:
        """ Returns current browser URL. """
        return self._web_driver.current_url

    def get_page_source(self) -> str:
        """ Returns current page body. """

        source = ''
        try:
            source = self._web_driver.page_source
        except Exception as e:
            print(f'Can not get page source', {e})

        return source

    def check_js_errors(self, ignore_list: list = None):
        """ This function checks JS errors on the page. """

        ignore_list = ignore_list or []

        logs = self._web_driver.get_log('browser')
        for log_message in logs:
            if log_message['level'] != 'WARNING':
                ignore = False
                for issue in ignore_list:
                    if issue in log_message['message']:
                        ignore = True
                        break

                assert ignore, 'JS error "{0}" on the page!'.format(log_message)

    def wait_page_loaded(self, timeout: int = 10) -> None:
        """
        Wait until page is loaded.
        :@param timeout: timeout in seconds
        """

        WebDriverWait(self._web_driver, timeout=timeout).until(
            lambda wd: self._web_driver.execute_script("return document.readyState") == 'complete',
            PageTookTooLongToResponseException(self._url, timeout)
        )
