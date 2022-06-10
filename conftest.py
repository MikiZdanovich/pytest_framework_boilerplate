def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="chrome",
                     help="Browser to run tests")