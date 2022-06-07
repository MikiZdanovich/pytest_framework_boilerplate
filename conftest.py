def pytest_addoption(parser):
    parser.addoption("--browser",
                     action="store",
                     default="firefox",
                     help="Browser to run tests")