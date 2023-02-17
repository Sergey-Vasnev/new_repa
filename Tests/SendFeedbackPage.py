from selenium.webdriver.common.by import By
from Framework.BasePage import BasePage
from Framework.Label import Label
from URLs import URLs


class SendFeedbackPage(BasePage):

    UNIQUE_LOCATOR = (By.XPATH, "//h1")

    def __init__(self):
        super().__init__(locator=self.UNIQUE_LOCATOR)

    def is_opened(self):
        return Label(self.UNIQUE_LOCATOR).element_is_present()

    def is_closed(self):
       return Label(self.UNIQUE_LOCATOR).element_is_not_present()