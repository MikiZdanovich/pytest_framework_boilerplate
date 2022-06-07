import pytest
from src.utils.driver_factory import DriverFactory


def pytest_generate_tests(metafunc):
    if "browser" in metafunc.fixturenames:
        if "all" in metafunc.config.getoption("browser"):
            metafunc.parametrize("browser", DriverFactory.SUPPORTED_BROWSERS)
        else:
            metafunc.parametrize("browser", [metafunc.config.getoption("browser")])


@pytest.fixture
def driver(browser):
    driver = DriverFactory.get_driver(browser)

    yield driver

    driver.quit()
