import sys

import pytest
from selenium import webdriver
from Singleton import Singleton
from Logger import Logg
logger=Logg()

class Driver(metaclass=Singleton):
    @staticmethod
    def chooseDriver(browser_name):
        logger.makeLog("=======================SEPARATOR=================================")
        logger.makeLog(browser_name)
        if browser_name == "chrome":
            options = webdriver.ChromeOptions()
            logger.makeLog("1")
            print("\nstart chrome browser for test..")
            # sys.exit()
            return webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            options = webdriver.FirefoxOptions()
            logger.makeLog("2")
            print("\nstart firefox browser for test..")
            browser = webdriver.Firefox(options=options)
            # sys.exit()
            return browser
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
