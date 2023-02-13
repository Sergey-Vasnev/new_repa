class BrowserConfig(object):
    BROWSER_NAME = "chrome"

    # функция ниже задумывалась для изменения BROWSER_NAME
    # в случае получения флага с помощью parser, но что-то пошло не так:с
    def change_browser_name(self,browser_name=None):
        if browser_name:
            self.BROWSER_NAME=browser_name

