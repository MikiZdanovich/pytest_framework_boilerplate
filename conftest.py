import pytest


def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Browser to run tests")


@pytest.fixture(scope="session")
def root_dir(request):
    return request.config.rootdir.strpath
