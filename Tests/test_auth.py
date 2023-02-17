import pytest
from Tests.HomePage import HomePage
from Tests.LoginPage import LoginPage
from Tests.WelcomePage import WelcomePage
from Framework.Logger import Logg
from Framework.Browser import Browser

logger=Logg("test_auth")


@pytest.mark.parametrize("login, password, typ",
                        [
                            ("admin", "admin", True),
                            ("Sssnake!", "", False),
                            ("naruto", "uzumaki", False)
                        ]
                        )
def test_auth(browser,login, password, typ):

    logger.make_DEBUG("__Test auth__")
    home_page=HomePage()
    welcome_page=WelcomePage()
    login_page=LoginPage()

    home_page.click_on_the_log_in_link_button()
    assert login_page.is_opened()
    logger.make_DEBUG(text="Authorization page opened")
    login_page.log_in(login, password)
    logger.make_DEBUG(text="Data entered and send")
    if typ == True:
        assert welcome_page.is_opened(), "Welcome page was not opened"
        logger.make_DEBUG(text="Welcome page is opened")
    else:
        if not password:
            assert Browser.catch_alert(), "Notification did not appear"
            logger.make_DEBUG(text="Notification of blank password accepted")
        assert welcome_page.is_closed()