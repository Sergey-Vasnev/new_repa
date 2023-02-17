from abc import ABC, abstractmethod
from Framework.BaseElement import BaseElement


class BasePage(ABC):
    """
    Abstract class for pages.

    ...

    Methods
    -------
    is_opened(locator='locator')
        Checks if the page with the specified unique locator is opened.

    is_opened(locator='locator')
        Checks if the page with the specified unique locator is closed.

    """

    def __init__(self, locator):
        '''
        Attributes
        ----------
        locator : Any
            Unique locator for the page.
        '''
        self.Locator = locator

    def is_opened(self):
        '''
        Checks if the page is opened.
        '''
        if BaseElement(self.Locator).element_is_present():
            return True

    def is_closed(self):
        '''
        Checks if the page is closed.
        '''
        if BaseElement(self.Locator).element_is_not_present():
            return True

    @abstractmethod
    def return_page_url(self):
        pass


