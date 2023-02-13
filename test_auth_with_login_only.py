import pytest
from LoginPage import LoginPage
from HomePage import HomePage
from Browser import Browser
from Framework.Button import Button
from Logger import Logg

logger=Logg()

@pytest.mark.parametrize('login',
                        [
                            ('Sssnake!')
                        ]
                        )

def test_invalid_auth(browser,login):
    logger.makeLog('__Тест на ввод Логина__')
    Browser.go_to_site(HomePage.URL)
    login_page=LoginPage(LoginPage.USERNAME_LOCATOR)
    #if HomePage(HomePage.UNIQUE_LOCATOR).is_opened():
    logger.makeLog(text='Главная страница открыта')
    Button(HomePage.LOGIN_BUTTON_LOCATOR).click_the_element()
    if login_page.is_opened():
        logger.makeLog(text='Страница для авторизации открыта')
    login_page.enter_username(login)
    login_page.click_on_the_submit_button()
    Browser.get_driver().switch_to.alert.accept()
    assert LoginPage(LoginPage.USERNAME_LOCATOR).is_opened()