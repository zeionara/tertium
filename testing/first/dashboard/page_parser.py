import sys
import os
from os import path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from page_parser_general import PageParserGeneral

class PageParser(PageParserGeneral):

    def __init__(self, driver):
        self.driver = driver

    def get_dismiss_titles(self):
        return self.driver.find_elements_by_class_name("tumblelog_title");

    def get_following(self):
        following = []
        for item in self.driver.find_elements_by_class_name("name-link"):
            following.append(item.text)
        return following

    def get_follower_links(self):
        return self.driver.find_elements_by_class_name("follow_list_item_blog")

    def get_reblog_text_field(self):
        return self.driver.find_element_by_class_name('editor-richtext')

    def get_post_avatar_link(self):
        return self.driver.find_element_by_class_name('post_avatar_link')