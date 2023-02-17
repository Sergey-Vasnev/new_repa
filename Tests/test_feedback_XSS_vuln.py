from Tests.FeedbackPage import FeedbackPage
from Tests.HomePage import HomePage
from Framework.Browser import Browser
from Framework.Logger import Logg

logger=Logg("test_feedback_xss_vuln")


def test_feedback_xss_vuln(browser):
    home_page = HomePage()
    feedback_page = FeedbackPage()
    logger.make_DEBUG("__start of the Test feedback XSS vuln__")
    home_page.click_on_the_feedback_link_button()
    assert feedback_page.is_opened()
    logger.make_DEBUG(text="Feedback page opened")
    feedback_page.enter_name("<script>alert('attack')</script>")
    logger.make_DEBUG(text="JavaScript command entered in the name field")
    feedback_page.click_on_the_submit_button()
    logger.make_DEBUG(text="Button pressed, data sent")
    if Browser.alert_presence():
        if Browser.get_text_from_alert() == "attack":
            assert False
    else:
        assert True
