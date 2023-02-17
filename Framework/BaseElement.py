from abc import ABC, abstractmethod
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Framework.Browser import Browser


class BaseElement(ABC):
    """
    Abstract class for locator.

    ...

    Methods
    -------
    find_element(time='1')
    Search element.

    find_elements(time=1)
    Search elements.

    element_is_present()
    Checks whether an element is on the page.

    element_is_not_present()
    Checks whether an element is NOT on the page.

    click_the_element()
    Clicks on the element.

    """
    # driver = Browser.get_driver()

    def __init__(self,locator):
        '''
        Attributes
        ----------
        locator : Any
            Locator to interact with.
        '''
        self.locator=locator

    def wait_for_element(self, time=1):
        '''
        Attributes
        ----------
        time : int
           Max time for searching.
        ...
        Return
        ----------
        Returns an element.
        '''
        WebDriverWait(Browser.get_driver(),time).until(EC.presence_of_element_located(self.locator))

    def wait_for_elements(self, time=1):
        '''
        Attributes
        ----------
        time : int
           Max time for searching.
        ...
        Returns
        ----------
        Returns an array.
        '''
        WebDriverWait(Browser.get_driver(),time).until(EC.presence_of_all_elements_located(self.locator))


    def element_is_present(self):
        '''
        Return True if element is on the page.
        '''
        return len(self.wait_for_elements()) > 0

    def element_is_not_present(self):
        '''
        Return True if TimeoutException was raised -> element is not on the page.
        '''
        try:
            self.wait_for_elements()
        except TimeoutException:
            return True

    def click_the_element(self):
        element=self.wait_for_element()
        element.click()

    @abstractmethod
    def get_class_name(self):
        return self.__name__

