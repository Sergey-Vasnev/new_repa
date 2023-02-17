from Tests.FeedbackPage import FeedbackPage
from Tests.HomePage import HomePage
from Tests.SendFeedbackPage import SendFeedbackPage
from Framework.Logger import Logg

logger=Logg('test_feedback_sending_only_with_name')


def test_feedback_sending_only_with_name(browser):

    logger.make_debug("__Test sending feedback only with a name__")
    home_page = HomePage()
    feedback_page = FeedbackPage()
    send_feedback_page = SendFeedbackPage()

    home_page.click_on_the_feedback_link_button()
    assert feedback_page.is_opened()
    logger.make_debug(text="Feedback page opened")
    feedback_page.enter_name("Sergey")
    logger.make_debug(text="Only name entered")
    feedback_page.click_on_the_submit_button()
    logger.make_debug(text="Button pressed, data sent")
    assert send_feedback_page.is_closed()