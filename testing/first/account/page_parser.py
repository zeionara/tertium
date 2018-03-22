import sys
import os
from os import path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from page_parser_general import PageParserGeneral

class PageParser(PageParserGeneral):

    def __init__(self, driver):
        self.driver = driver

    def get_language_selector(self):
        return self.driver.find_element_by_id('user_language')