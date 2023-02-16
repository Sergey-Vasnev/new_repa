import pytest
from Framework.Browser import Browser
from Tests.HomePage import HomePage
from Tests.LoginPage import LoginPage
from Framework.Logger import Logg

logger=Logg(str('test_auth_with_entered_login_and_empty_password'))

@pytest.mark.parametrize('login',
                        [
                            ('Sssnake!')
                        ]
                        )

def test_auth_with_entered_login_and_empty_password(browser,login):

    logger.make_log('__Test with entered login and empty password__')
    #Browser.go_to_site(HomePage.URL)
    #logger.makeLog(text='Home page opened')
    HomePage().click_on_the_log_in_link_button()
    login_page=LoginPage()
    assert login_page.is_opened()
    logger.make_log(text='Authorization page opened')
    login_page.enter_username(login)
    logger.make_log(text='Only login entered')
    login_page.click_on_the_submit_button()
    logger.make_log(text='Button pressed, data sent')
    if Browser.catch_alert():
        logger.make_log(text='Notification of blank password accepted')
    assert login_page.is_opened()