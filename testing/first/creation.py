import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from subprocess import call
from random import randint

from utils import PostOperator, PresenceChecker, ButtonGetter

URL = "https://www.tumblr.com/"

SESSION_URL = os.environ['SESSION_URL']
SESSION_ID = os.environ['SESSION_ID']

class CreationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor = SESSION_URL, desired_capabilities={})
        self.driver.session_id = SESSION_ID
        print('called:', call(['xdotool','getwindowfocus','windowkill']))
        self.driver.get(URL + "/dashboard")

    def tearDown(self):
        pass
        #self.driver.close()

    ## new text post

    def get_text_post_title_input_field(self):
        return self.driver.find_element_by_class_name('title-field').find_element_by_class_name('editor-plaintext')

    def get_text_post_description_input_field(self):
        return self.driver.find_element_by_class_name('caption-field').find_element_by_class_name('editor-richtext')

    def get_text_post_tag_input_field(self):
        return self.driver.find_element_by_class_name('post-form--tag-editor').find_element_by_class_name('editor-plaintext')

    def get_posted_count(self):
        self.driver.find_element_by_id('account_button').click()
        time.sleep(1)
        try:
            for item in self.driver.find_elements_by_class_name('blog-sub-nav-item-link'):
                if item.find_element_by_class_name('blog-sub-nav-item-label').text == 'Posts':
                    return int(str(item.find_element_by_class_name("blog-sub-nav-item-data").text))
        finally:
            self.driver.find_element_by_id('account_button').click()
        

#@unittest.skip("skipping")
class PlainTextTest(CreationTest):

    def test_creation_post_with_plain_text(self):
        driver = self.driver

        button_getter = ButtonGetter(driver)
        post_operator = PostOperator(driver)

        post_title = 'Hello world'

        post_body = 'Lorem ipsum dolor sit amet'

        post_hashes = '#test'

        posted_count_before_adding_post = self.get_posted_count()

        button_getter.get_create_button().click()

        time.sleep(1)

        button_getter.get_post_type_selection_button('text').click()

        time.sleep(1)

        self.get_text_post_title_input_field().send_keys(post_title)
        self.get_text_post_description_input_field().send_keys(post_body)
        self.get_text_post_tag_input_field().send_keys(post_hashes)

        driver.execute_script("document.getElementsByClassName('create_post_button')[0].click()")

        time.sleep(1)

        driver.refresh()

        posted_count_after_adding_post = self.get_posted_count()

        assert posted_count_after_adding_post == posted_count_before_adding_post + 1

        time.sleep(1)

        button_getter.get_account_button().click()
        
        time.sleep(1)

        button_getter.get_posts_button().click()

        added_post = post_operator.get_text_post(post_title, post_body)

        assert added_post is not None

        post_operator.get_control_menu_button(added_post).click()

        time.sleep(0.5)

        post_operator.get_delete_button(added_post).click()

        time.sleep(1)

        driver.find_element_by_class_name("btn_1").click()

        time.sleep(1)

        driver.refresh()

        assert post_operator.get_text_post(post_title, post_body) is None

        posted_count_after_deleting_post = self.get_posted_count()

        assert posted_count_after_adding_post == posted_count_after_deleting_post + 1

if __name__ == "__main__":
    unittest.main()