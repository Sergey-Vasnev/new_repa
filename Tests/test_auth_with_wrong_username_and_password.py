import pytest
from Tests.HomePage import HomePage
from Tests.LoginPage import LoginPage
from Tests.WelcomePage import WelcomePage
from Framework.Logger import Logg

logger=Logg('test_auth_with_wrong_username_and_password')


@pytest.mark.parametrize('login, password',
                        [
                            ('naruto','uzumaki')
                        ]
                        )
def test_auth_with_wrong_username_and_password(browser,login,password):

    logger.make_log('__Test with wrong username and password__')
    #Browser.go_to_site(HomePage.URL)
    #logger.makeLog(text='Home page opened')
    HomePage().click_on_the_log_in_link_button()
    assert LoginPage().is_opened()
    logger.make_log(text='Authorization page opened')
    LoginPage().log_in(login, password)
    logger.make_log(text='Data entered')
    assert WelcomePage().is_closed()