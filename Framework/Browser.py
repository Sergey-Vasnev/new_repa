from selenium.common import NoAlertPresentException
from Framework.Singleton import Singleton
from Framework.BrowserFactory import BrowserFactory


class Browser(metaclass=Singleton):

    #driver = None
    # def __init__(self):
    #     self.driver = Driver.choose_driver(BrowserConfig.BROWSER_NAME)

    @classmethod
    def driver_init(cls,browser_name):
        cls.driver = BrowserFactory.choose_driver(browser_name)

    @classmethod
    def get_driver(cls):
        return cls().driver

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
    def refresh(cls):
        cls.get_driver().refresh()

    @classmethod
    def switch_to_alert_and_read_its_msg(cls):
            cls.get_driver().switch_to.alert()
            return cls.get_driver().alert().getText()

    @classmethod
    def catch_alert(cls):
        try:
            cls.get_driver().switch_to.alert.accept()
            return True
        except NoAlertPresentException:
            return False

    @classmethod
    def catch_text_from_alert(cls):
        pass
