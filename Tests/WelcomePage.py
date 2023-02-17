from selenium.webdriver.common.by import By
from Framework.BasePage import BasePage
from Framework.List import List
from URLs import URLs


class WelcomePage(BasePage):

    # a unique locator
    # that can be used to verify that this is the right page
    UNIQUE_LOCATOR = (By.ID, "listAccounts")

    def __init__(self):
        super().__init__(locator=self.UNIQUE_LOCATOR)

    def is_opened(self):
        List(self.UNIQUE_LOCATOR).element_is_present()

    def is_closed(self):
        List(self.UNIQUE_LOCATOR).element_is_not_present()
