from abc import ABC
from Framework.BaseElement import BaseElement

class BasePage(ABC):
    def __init__(self,locator):
        self.Locator=locator

    def is_opened(self):
        if BaseElement(self.Locator).element_is_present():
            return True

    def is_closed(self):
        if BaseElement(self.Locator).element_is_not_present():
            return True

'''   @abstractmethod
    def return_locator(self):
        return self.Locator'''
