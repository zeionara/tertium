import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from subprocess import call
from random import randint
import sys
from os import path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from page_parser import PageParser
from button_getter import ButtonGetter
from post_operator import PostOperator
from action_handler import ActionHandler

URL = "https://www.tumblr.com"

SESSION_URL = os.environ['SESSION_URL']
SESSION_ID = os.environ['SESSION_ID']

class CreationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor = SESSION_URL, desired_capabilities={})
        self.driver.session_id = SESSION_ID
        call(['xdotool','getwindowfocus','windowkill'])
        self.driver.get(URL + "/dashboard")

    def tearDown(self):
        pass

#@unittest.skip("skipping")
class PlainTextTest(CreationTest):

    def test_creation_post_with_plain_text(self):
        driver = self.driver

        button_getter = ButtonGetter(driver)
        post_operator = PostOperator(driver)
        page_parser = PageParser(driver)
        action_handler = ActionHandler(driver)

        post_title = 'Hello world'

        post_body = 'Lorem ipsum dolor sit amet'

        post_hashes = '#test'

        posted_count_before_adding_post = page_parser.get_posted_count()

        button_getter.get_create_button().click()

        time.sleep(1)

        button_getter.get_post_type_selection_button('text').click()

        time.sleep(1)

        page_parser.get_text_post_title_input_field().send_keys(post_title)
        page_parser.get_text_post_description_input_field().send_keys(post_body)
        page_parser.get_text_post_tag_input_field().send_keys(post_hashes)

        action_handler.click_confirm_post()

        time.sleep(1)

        driver.refresh()

        posted_count_after_adding_post = page_parser.get_posted_count()

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

        button_getter.get_ok_button().click()

        time.sleep(1)

        driver.refresh()

        assert post_operator.get_text_post(post_title, post_body) is None

        posted_count_after_deleting_post = page_parser.get_posted_count()

        assert posted_count_after_adding_post == posted_count_after_deleting_post + 1

if __name__ == "__main__":
    unittest.main()