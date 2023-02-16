from selenium.webdriver.common.by import By
from Framework.BasePage import BasePage
from Framework.Button import Button


class HomePage(BasePage):

    # a unique locator
    # that can be used to verify that this is the right page
    UNIQUE_LOCATOR=r'//a[contains(@href,"personal_savi")]'

    # page address
    URL='http://testfire.net/index.jsp'

    # locators of the links to other pages
    LOGIN_BUTTON_LOCATOR = (By.ID, "LoginLink")
    FEEDBACK_BUTTON_LOCATOR = (By.XPATH, "//a[contains(@href,'eedb')]")

    def __init__(self):
        super().__init__(locator=self.UNIQUE_LOCATOR)

    def click_on_the_log_in_link_button(self):
        button = Button(self.LOGIN_BUTTON_LOCATOR)
        button.click_the_element()

    def click_on_the_feedback_link_button(self):
        button = Button(self.FEEDBACK_BUTTON_LOCATOR)
        button.click_the_element()


