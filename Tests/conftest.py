import pytest
from Framework.Browser import Browser
from Framework.Logger import Logg
from Framework.browser_config import BrowserConfig


logger=Logg(f'PrePost_conditions')


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    BrowserConfig.BROWSER_NAME=browser_name
    base_url = "http://testfire.net/"
    Browser().driver_init(browser_name=browser_name)
    Browser.go_to_site(base_url)
    logger.make_log(text='Home page opened')
    yield
    Browser.quit()
