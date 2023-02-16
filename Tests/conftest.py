import pytest
from Framework.Browser import Browser
from Framework.Logger import Logg
from Framework.browser_config import BrowserConfig
from URLs import URLs


logger=Logg(f'PrePost_conditions')


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser_name")
    BrowserConfig.BROWSER_NAME=browser_name
    Browser().driver_init(browser_name=browser_name)
    Browser.go_to_site(URLs.HOME_PAGE_URL)
    logger.make_log(text='Home page opened')
    yield
    Browser.quit()
