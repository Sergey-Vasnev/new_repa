class BrowserConfig(object):

    BROWSER_NAME = "chrome"

    def change_browser_name(self,browser_name=None):
        if browser_name:
            self.BROWSER_NAME=browser_name
