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

from post_operator import PostOperator
from button_getter import ButtonGetter

CHROME_DRIVER_LOCATION = './chromedriver'
URL = "https://www.tumblr.com"

INITIAL_NUMBER_OF_POSTS_TO_SHOW = 38

FOLLOWING_INDEX = 3
FIRST_POST_INDEX = 2

MIN_NUMBER_OF_POSTS = 10

SESSION_URL = os.environ['SESSION_URL']
SESSION_ID = os.environ['SESSION_ID']

class DiscoverTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor = SESSION_URL, desired_capabilities={})
        self.driver.session_id = SESSION_ID
        call(['xdotool','getwindowfocus','windowkill'])
        self.driver.get(URL + "/dashboard")

    def tearDown(self):
        pass

#@unittest.skip("skipping")
class CategoriesTest(DiscoverTest):

    def test_switching_categories_succeeded(self):
        driver = self.driver

        button_getter = ButtonGetter(driver)
        post_operator = PostOperator(driver)

        button_getter.get_discover_button().click()

        for button in button_getter.get_discover_types_buttons():
            if (button.is_displayed()):
                button.click()
                time.sleep(2)
                assert len(post_operator.get_posts()) >= MIN_NUMBER_OF_POSTS

#@unittest.skip("skipping")
class QueriesTest(DiscoverTest):

    def test_popular_queries_succeeded(self):
        driver = self.driver

        button_getter = ButtonGetter(driver)
        post_operator = PostOperator(driver)

        button_getter.get_discover_button().click()

        discover_search_buttons = button_getter.get_discover_search_buttons()
        button_index = randint(0, len(discover_search_buttons) - 1)

        query = discover_search_buttons[button_index].text

        discover_search_buttons[button_index].click()

        assert query.lower().replace(' ','%20') in driver.current_url.lower()

        assert len(post_operator.get_posts()) >= MIN_NUMBER_OF_POSTS

if __name__ == "__main__":
    unittest.main()