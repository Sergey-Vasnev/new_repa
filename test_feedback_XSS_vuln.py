from selenium.common import NoAlertPresentException

from FeedbackPage import FeedbackPage
from HomePage import HomePage
from Browser import Browser
from Framework.Button import Button
from SendFeedbackPage import SendFeedbackPage
from Logger import Logg

logger=Logg()

def test_feedback_XSS_vuln(browser):
    logger.makeLog('__Test feedback XSS vuln__')
    Browser.go_to_site(HomePage.URL)
    logger.makeLog(text='Home page opened')
    HomePage().click_on_the_feedback_link_button()
    if FeedbackPage().is_opened():
        logger.makeLog(text='Feedback page opened')
    FeedbackPage().enter_name("<script>alert('attack')</script>")
    logger.makeLog(text='JavaScript command entered in the name field')
    FeedbackPage().click_on_the_submit_button()
    logger.makeLog(text='Button pressed, data sent')
    assert Browser.catch_alert()