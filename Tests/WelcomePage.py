from selenium.webdriver.common.by import By
from Framework.BasePage import BasePage


class WelcomePage(BasePage):

    # a unique locator
    # that can be used to verify that this is the right page
    UNIQUE_LOCATOR = (By.ID, "listAccounts")

    def __init__(self):
        super().__init__(locator=self.UNIQUE_LOCATOR)
