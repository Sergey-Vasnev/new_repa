from Framework.BaseElement import BaseElement


class TextBox(BaseElement):  # class for textbox elements

    def enter_data(self,data):  # enter values into the textbox
        element = self.wait_for_element()
        element.click()
        element.send_keys(data)

    def get_class_name(self):
        pass
