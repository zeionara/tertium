import sys
import os
from os import path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from page_parser_general import PageParserGeneral

class PageParser(PageParserGeneral):

    def __init__(self, driver):
        self.driver = driver

    def get_text_post_title_input_field(self):
        return self.driver.find_element_by_class_name('title-field').find_element_by_class_name('editor-plaintext')

    def get_text_post_description_input_field(self):
        return self.driver.find_element_by_class_name('caption-field').find_element_by_class_name('editor-richtext')

    def get_text_post_tag_input_field(self):
        return self.driver.find_element_by_class_name('post-form--tag-editor').find_element_by_class_name('editor-plaintext')