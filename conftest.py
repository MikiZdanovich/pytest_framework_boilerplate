import pytest
from src.utils.driver_factory import DriverFactory


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="firefox",
                     help="Browser to run tests")


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser").lower()


# @pytest.fixture(scope='session')
# def config(request):
#     root_dir = str(request.config.rootdir)
#     with open(os.path.join(root_dir, CONFIG_PATH)) as config_file:
#         return json.load(config_file)


@pytest.fixture
def driver(browser_name):
    driver = DriverFactory.get_driver(browser_name)

    yield driver

    driver.quit()
