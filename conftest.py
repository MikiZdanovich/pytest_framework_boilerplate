import os
import json
import pytest

from src.utils.driver_factory import DriverFactory

CONFIG_PATH = "src/configuration/config.json"
SUPPORTED_BROWSERS = ["chrome", "firefox", "edge"]


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Browser to run tests")


@pytest.fixture(scope='session')
def config(request):
    root_dir = str(request.config.rootdir)
    with open(os.path.join(root_dir, CONFIG_PATH)) as config_file:
        browser_name = request.config.getoption("--browser")
        return json.load(config_file)[browser_name]


@pytest.fixture(scope="session")
def browser_setup(config):
    if "browser" not in config:
        raise Exception('The configuration file does not contain "browser"')
    elif config["browser"] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config["browser"]


@pytest.fixture
def driver(config):
    driver = DriverFactory.get_driver(config["browser"], config["headless_mode"])

    yield driver

    driver.quit()
