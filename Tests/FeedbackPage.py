from selenium.webdriver.common.by import By
from Framework.BasePage import BasePage
from Framework.TextBox import TextBox
from Framework.Button import Button
from URLs import URLs

class FeedbackPage(BasePage):

    YOUR_NAME_LOCATOR = (By.NAME, "name")  # creates locator for Your Name field
    YOUR_EMAIL_LOCATOR = (By.NAME, "email_addr")  # creates locator for Your Email Address field
    SUBJECT_LOCATOR = (By.NAME, "subject")  # creates locator for YSubject field
    COMMENTS_LOCATOR = (By.NAME, "comments")  # creates locator for Question/Comment field
    BUTTON_LOCATOR = (By.NAME, "submit")

    def __init__(self):
        super().__init__(locator=self.YOUR_NAME_LOCATOR)

    def enter_name(self, name):
        TextBox(self.YOUR_NAME_LOCATOR).enter_data(name)

    def enter_email(self, email):
        TextBox(self.YOUR_EMAIL_LOCATOR).enter_data(email)

    def enter_comments(self, comments):
        TextBox(self.COMMENTS_LOCATOR).enter_data(comments)

    def enter_subject(self, subject):
        TextBox(self.SUBJECT_LOCATOR).enter_data(subject)

    def click_on_the_submit_button(self):
        Button(self.BUTTON_LOCATOR).click_the_element()

    def fill_the_feedback_form(self, name, email, subject, comments):
        TextBox(self.YOUR_EMAIL_LOCATOR).enter_data(name)
        TextBox(self.YOUR_EMAIL_LOCATOR).enter_data(email)
        TextBox(self.SUBJECT_LOCATOR).enter_data(subject)
        TextBox(self.COMMENTS_LOCATOR).enter_data(comments)
        Button(self.BUTTON_LOCATOR).click_the_element()

    def is_opened(self):
        return TextBox(self.YOUR_NAME_LOCATOR).element_is_present()

    def is_closed(self):
        return TextBox(self.YOUR_NAME_LOCATOR).element_is_not_present()
