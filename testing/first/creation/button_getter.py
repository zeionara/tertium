import sys
import os
from os import path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from button_getter_general import ButtonGetterGeneral

class ButtonGetter(ButtonGetterGeneral):

    def __init__(self, driver):
        self.driver = driver

    def get_create_button(self):
        return self.driver.find_element_by_class_name('compose-button')

    def get_post_type_selection_button(self, post_type):
        for button in self.driver.find_elements_by_class_name('tab-post-type'):
            if (button.get_attribute('data-post-type') == post_type):
                return button

