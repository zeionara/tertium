import sys
import os
from os import path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from button_getter_general import ButtonGetterGeneral

class ButtonGetter(ButtonGetterGeneral):

    def __init__(self, driver):
        self.driver = driver

    def get_follow_buttons(self):
        return self.driver.find_elements_by_class_name("plus-follow-button")

    def get_unfollow_button(self, follower):
        return self.driver.find_element_by_id("unfollow_button_"+follower)

    def get_like_button(self, post):
        return post.find_element_by_class_name("like")

    def get_like_button_by_post_id(self, post_operator, post_id):
        for post in post_operator.get_posts():
            if post_operator.get_post_id(post) == post_id:
                return self.get_like_button(post)

    def get_dismiss_buttons(self):
        return self.driver.find_elements_by_class_name("dismiss")

    def get_permalink_button(self):
        return self.driver.find_element_by_class_name('messaging-share-post-external-network')

    def get_embed_button(self):
        return self.driver.find_element_by_class_name('network--embed')

    def get_report_button(self):
        return self.driver.find_element_by_class_name('network--flag')

    def get_share_button(self, post):
        return post.find_element_by_class_name('share')

    def get_reblog_button(self, post):
        return post.find_element_by_class_name('reblog')

    def get_reblog_applying_button(self):
        return self.driver.find_element_by_class_name('create_post_button')