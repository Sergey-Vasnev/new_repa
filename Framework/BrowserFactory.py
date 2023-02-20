from selenium import webdriver


class BrowserFactory():

    @staticmethod
    def choose_driver(browser_name):
        if browser_name == "chrome":
            return webdriver.Chrome()

        elif browser_name == "firefox":
            return webdriver.Firefox()

        else:
            raise RuntimeError("--browser_name flag should be chrome or firefox")
