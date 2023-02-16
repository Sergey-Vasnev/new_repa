from Tests.FeedbackPage import FeedbackPage
from Tests.HomePage import HomePage
from Framework.Browser import Browser
from Framework.Logger import Logg

logger=Logg('test_feedback_xss_vuln')


def test_feedback_xss_vuln(browser):

    logger.make_log('__Test feedback XSS vuln__')
    #Browser.go_to_site(HomePage.URL)
    #logger.makeLog(text='Home page opened')
    HomePage().click_on_the_feedback_link_button()
    assert FeedbackPage().is_opened()
    logger.make_log(text='Feedback page opened')
    FeedbackPage().enter_name("<script>alert('attack')</script>")
    logger.make_log(text='JavaScript command entered in the name field')
    FeedbackPage().click_on_the_submit_button()
    logger.make_log(text='Button pressed, data sent')
    assert Browser.catch_alert()