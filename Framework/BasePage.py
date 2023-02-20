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

    @abstractmethod
    def is_opened(self):
        '''
        Checks if the page is opened.
        '''
        # return BaseElement(self.Locator).element_is_present()
        pass

    @abstractmethod
    def is_closed(self):
        '''
        Checks if the page is closed.
        '''
        # return BaseElement(self.Locator).element_is_not_present()
        pass



