from Singleton import Singleton
from Driver import Driver
from browser_config import BrowserConfig
from Logger import Logg
logger=Logg()

class Browser(metaclass=Singleton):

    driver = None
    # def __init__(self):
    #     self.driver = "sdfsdf"

    #driver = Driver.chooseDriver(BrowserConfig.BROWSER_NAME)
    @classmethod
    def driver_init(cls,browser_name=BrowserConfig.BROWSER_NAME):
        cls.driver=Driver.chooseDriver(browser_name)

    @classmethod
    def get_driver(self):
        return self.driver

    @classmethod
    def quit(self):
        self.get_driver().quit()

    # function to go to the specified url
    @classmethod
    def go_to_site(cls,base_url):
        logger.makeLog(str(cls.get_driver()))
        return cls.get_driver().get(base_url)
    
    # function to return the current url
    @classmethod
    def current_url(self):
        return self.driver.current_url

    @classmethod
    def refresh(self,driver):
        driver.switch_to.alert.accept()
