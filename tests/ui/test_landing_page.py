import pytest
from pytest import mark

from data.pages.demoqa_landing_page import LandingPage


@mark.landing_page
@mark.ui
class LandingPageSuite:
    """This is sample test case"""

    @pytest.fixture(autouse=True)
    def landing_page(self, driver):
        return LandingPage(driver).open()

    @mark.smoke
    def test_header_text(self, landing_page):
        expected_header_text = 'Welcome to the-internet'
        assert landing_page.heading_text == expected_header_text
