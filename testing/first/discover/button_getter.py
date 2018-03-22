import sys
import os
from os import path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from button_getter_general import ButtonGetterGeneral

class ButtonGetter(ButtonGetterGeneral):

    def __init__(self, driver):
        self.driver = driver

    def get_discover_types_buttons(self):
        return self.driver.find_element_by_class_name('types-tabs').find_elements_by_class_name('content-control')

    def get_discover_search_buttons(self):
        return self.driver.find_element_by_class_name('discover-search-terms').find_elements_by_class_name('discover-search-term')