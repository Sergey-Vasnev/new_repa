import pytest
from selenium import webdriver
from Framework.Singleton import Singleton


class Driver(metaclass = Singleton):

    @staticmethod
    def choose_driver(browser_name):
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            print("\nstart chrome browser for test..")
            return webdriver.Chrome(options=options)

        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            print("\nstart firefox browser for test..")
            return webdriver.Firefox(options=options)

        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
