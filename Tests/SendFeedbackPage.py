from selenium.webdriver.common.by import By
from Framework.BasePage import BasePage
from URLs import URLs


class SendFeedbackPage(BasePage):

    UNIQUE_LOCATOR = (By.XPATH, "//h1")

    def __init__(self):
        super().__init__(locator=self.UNIQUE_LOCATOR)

    def get_class_name(self):
        pass