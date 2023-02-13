import pytest
from LoginPage import LoginPage
from WelcomePage import WelcomePage
from HomePage import HomePage
from Browser import Browser
from Framework.Button import Button
from Logger import Logg

logger=Logg()

@pytest.mark.parametrize('login, password',
                        [
                            ('naruto','uzumaki')
                        ]
                        )

def test_altoro_matual_invalid_auth(login,password):
    logger.makeLog('__Тест на ввод неправильного логина и пароля__')
    Browser.go_to_site(HomePage.URL)
    #if HomePage(HomePage.UNIQUE_LOCATOR).is_opened():
    logger.makeLog(text='Главная страница открыта')
    Button(HomePage.LOGIN_BUTTON_LOCATOR).click_the_element()
    if LoginPage(LoginPage.USERNAME_LOCATOR).is_opened():
        logger.makeLog(text='Страница для авторизации открыта')
    LoginPage(LoginPage.USERNAME_LOCATOR).log_in(login, password)
    assert WelcomePage(WelcomePage.UNIQUE_LOCATOR).is_closed()