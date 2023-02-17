from selenium.common import NoAlertPresentException
from Framework.Singleton import Singleton
from Framework.BrowserFactory import BrowserFactory


class Browser(metaclass=Singleton):

    @classmethod
    def driver_init(cls,browser_name):
        cls._driver = BrowserFactory.choose_driver(browser_name)

    @classmethod
    def get_driver(cls):
        return cls()._driver

    @classmethod
    def quit(cls):
        cls.get_driver().quit()

    # function to go to the specified url
    @classmethod
    def go_to_site(cls,base_url):
        cls.get_driver().get(base_url)
    
    # function to return the current url
    @classmethod
    def get_current_url(cls):
        return cls.get_driver().current_url

    @classmethod
    def refresh_the_page(cls):
        cls.get_driver().refresh()

    @classmethod
    def get_text_from_alert(cls):
        try:
            return cls.get_driver().switch_to.alert.text
        except NoAlertPresentException:
            return None

    @classmethod
    def alert_presence(cls):
        try:
            cls.get_driver().switch_to.alert
        except NoAlertPresentException:
            return False

    @classmethod
    def catch_alert(cls):
        try:
            cls.get_driver().switch_to.alert.accept()
            return True
        except NoAlertPresentException:
            return False
