from Framework.BaseElement import BaseElement

class TextBox(BaseElement):

    def enter_data(self,data):
        element = self.find_element()
        element.click()
        element.send_keys(data)