import pytest


from data.pages.demoqa_landing_page import LandingPage


class TestLandingPage:
    """This is sample test case"""

    @pytest.fixture(scope="function")
    def landing_page(self, driver, url='http://the-internet.herokuapp.com/'):
        return LandingPage(driver, url)

    def test_header_text(self, landing_page):
        expected_header_text = 'Welcome to the-internet'
        actual_header_text = landing_page.welcome_heading.get_text()
        assert actual_header_text == expected_header_text
