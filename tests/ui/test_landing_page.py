import pytest
from pytest import mark

from data.pages.demoqa_landing_page import LandingPage


@mark.landing_page
@mark.ui
class LandingPageSuite:
    """This is sample test case"""

    @pytest.fixture(autouse=True)
    def landing_page(self, driver):
        return LandingPage(driver)

    @mark.smoke
    def test_header_text(self, landing_page):
        expected_header_text = 'Welcome to the-internet'
        actual_header_text = landing_page.get_welcome_heading_text()
        assert actual_header_text == expected_header_text

