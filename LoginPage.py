from selenium.webdriver.common.by import By
from Framework.BasePage import BasePage
from Framework.TextBox import TextBox
from Framework.Button import Button

# functions for interacting with locators
class LoginPage(BasePage):

    USERNAME_LOCATOR = (By.NAME, "uid")  # locator for the username field
    PASSWORD_LOCATOR = (By.NAME, "passw")  # locator for the password field
    BUTTON_LOCATOR = (By.NAME, "btnSubmit")  # locator for submit button
    URL = "http://testfire.net/login.jsp"

    LoginPage=BasePage(USERNAME_LOCATOR)

    # function to input username
    def enter_username(self, username):
        username_field = TextBox(self.USERNAME_LOCATOR)  # search for the username field
        username_field.enter_data(username)

    # function to input password
    def enter_password(self, password):
        passw_field = TextBox(self.PASSWORD_LOCATOR)  # search for the password field
        passw_field.enter_data(password)

    # button click to send data
    def click_on_the_submit_button(self):
        button = Button(self.BUTTON_LOCATOR)
        button.click_the_element()

    def return_locator(self):
        pass

    def log_in(self, login, password):
        TextBox(self.USERNAME_LOCATOR).enter_data(login)
        TextBox(self.PASSWORD_LOCATOR).enter_data(password)
        Button(self.BUTTON_LOCATOR).click_the_element()







