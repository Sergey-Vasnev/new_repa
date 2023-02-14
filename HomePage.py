from selenium.webdriver.common.by import By
from Framework.BasePage import BasePage


class HomePage(BasePage):
    UNIQUE_LOCATOR=r'//a[contains(@href,"personal_savi")]'
    URL='http://testfire.net/index.jsp'
    LOGIN_BUTTON_LOCATOR = (By.ID, "LoginLink")

    def return_locator(self):
        pass
