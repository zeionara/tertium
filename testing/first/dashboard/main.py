import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from subprocess import call
import sys
from os import path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils import PostOperator, PresenceChecker, ButtonGetter

from page_parser import PageParser
from post_operator import PostOperator
from presence_checker import PresenceChecker
from button_getter import ButtonGetter

CHROME_DRIVER_LOCATION = './chromedriver'
URL = "https://www.tumblr.com"

INITIAL_NUMBER_OF_POSTS_TO_SHOW = 38

FOLLOWING_INDEX = 2
FIRST_POST_INDEX = 2

SESSION_URL = os.environ['SESSION_URL']
SESSION_ID = os.environ['SESSION_ID']

POST_NOTE = 'nice'

class DashboardTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor = SESSION_URL, desired_capabilities={})
        self.driver.session_id = SESSION_ID
        call(['xdotool','getwindowfocus','windowkill'])
        self.driver.get(URL + "/dashboard")

    def tearDown(self):
        pass

#@unittest.skip("skipping")
class FollowSuccess(DashboardTest):

    def test_follow_succeeded(self):
        driver = self.driver

        button_getter = ButtonGetter(driver)
        page_parser = PageParser(driver)

        follow_buttons = button_getter.get_follow_buttons()

        followed_title = follow_buttons[FOLLOWING_INDEX].get_attribute('data-tumblelog-name')
        follow_buttons[FOLLOWING_INDEX].send_keys(Keys.RETURN) #click

        self.driver.get(URL + "/following")

        assert followed_title in page_parser.get_following()

        button_getter.get_unfollow_button(followed_title).click()

        time.sleep(1)

        button_getter.get_ok_button().click()

        time.sleep(1)

        self.driver.refresh()

        assert followed_title not in page_parser.get_following()


#@unittest.skip("skipping")
class DismissSuccess(DashboardTest):

    def test_dismiss_succeeded(self):
        driver = self.driver

        button_getter = ButtonGetter(driver)
        page_parser = PageParser(driver)

        dismiss_buttons = button_getter.get_dismiss_buttons()
        dismiss_titles = page_parser.get_dismiss_titles()

        dismiss_buttons[FOLLOWING_INDEX].click()

        time.sleep(1)

        assert dismiss_titles[FOLLOWING_INDEX].text not in page_parser.get_dismiss_titles()

#@unittest.skip("skipping")
class ShowCommunityInfoSuccess(DashboardTest):

    def test_show_community_info(self):
        driver = self.driver

        presence_checker = PresenceChecker(driver)
        page_parser = PageParser(driver)

        assert not presence_checker.is_there_drawer_container()
        assert not presence_checker.is_there_glass_container()

        followers_links = page_parser.get_follower_links()
        followers_links[FOLLOWING_INDEX].send_keys(Keys.RETURN) #click

        assert presence_checker.is_there_drawer_container()
        assert presence_checker.is_there_glass_container()

#@unittest.skip("skipping")
class LikeSuccess(DashboardTest):

    def test_like_succeeded(self):
        driver = self.driver

        post_operator = PostOperator(driver)
        button_getter = ButtonGetter(driver)
        presence_checker = PresenceChecker(driver)
        page_parser = PageParser(driver)

        time.sleep(2)

        posts = post_operator.get_posts()

        old_liked_count = page_parser.get_liked_count(URL)
        like_button = button_getter.get_like_button(posts[FIRST_POST_INDEX + FOLLOWING_INDEX])
        post_id = post_operator.get_post_id(posts[FIRST_POST_INDEX + FOLLOWING_INDEX])

        like_button.click()

        time.sleep(1)

        assert 'liked' in like_button.get_attribute('class')

        self.driver.get(URL + "/likes")

        assert presence_checker.is_there_post(post_operator, post_id)

        new_liked_count = page_parser.get_liked_count(URL)
        
        assert new_liked_count == old_liked_count + 1

        time.sleep(2)

        button_getter.get_like_button_by_post_id(post_operator, post_id).click()

        driver.refresh()

        assert button_getter.get_like_button_by_post_id(post_operator, post_id) is None

        new_liked_count = page_parser.get_liked_count(URL)

        assert new_liked_count == old_liked_count

@unittest.skip("skipping")
class ShareSuccess(DashboardTest):

    def test_share_succeeded(self):
        driver = self.driver

        button_getter = ButtonGetter(driver)
        presence_checker = PresenceChecker(driver)
        post_operator = PostOperator(driver)

        post = post_operator.get_posts()[FIRST_POST_INDEX + FOLLOWING_INDEX]
        post_id = post_operator.get_post_id(post)
        button_getter.get_share_button(post).click()

        time.sleep(2)

        button_getter.get_permalink_button().click()
        assert presence_checker.is_there_tab_with_url_part(post_id)

        time.sleep(1)

        assert not presence_checker.is_there_item_with_class('back-button')
        assert not presence_checker.is_there_item_with_class('embed-code')
        button_getter.get_embed_button().click()

        time.sleep(1)

        assert presence_checker.is_there_item_with_class('back-button')
        assert presence_checker.is_there_item_with_class('embed-code')
        driver.find_element_by_class_name('back-button').click()

        time.sleep(1)

        assert not presence_checker.is_there_item_with_class('back-button')
        assert not presence_checker.is_there_item_with_class('embed-code')
        assert not presence_checker.is_there_glass_container()
        assert not presence_checker.is_there_drawer_container()

        button_getter.get_report_button().click()

        time.sleep(1)

        assert presence_checker.is_there_glass_container()
        assert presence_checker.is_there_drawer_container()

@unittest.skip("skipping")
class ReblogSuccess(DashboardTest):

    def test_reblog_succeeded(self):
        driver = self.driver

        button_getter = ButtonGetter(driver)
        presence_checker = PresenceChecker(driver)
        post_operator = PostOperator(driver)
        page_parser = PageParser(driver)

        post = post_operator.get_posts()[FIRST_POST_INDEX + FOLLOWING_INDEX]
        post_id = post_operator.get_post_id(post)

        old_posted_count = page_parser.get_posted_count()

        button_getter.get_reblog_button(post).click()

        time.sleep(1)

        assert presence_checker.is_there_post_modal_container()

        page_parser.get_reblog_text_field().send_keys(POST_NOTE)

        post_settings_button = button_getter.get_post_settings_button()

        assert not presence_checker.is_there_post_settings_dropdown()
        post_settings_button.click()

        time.sleep(1)

        assert presence_checker.is_there_post_settings_dropdown()
        post_settings_button.click()

        time.sleep(1)

        button_getter.get_reblog_applying_button().click()

        time.sleep(2)

        new_posted_count = page_parser.get_posted_count()

        assert old_posted_count + 1 == new_posted_count

        self.driver.get(page_parser.get_post_avatar_link().get_attribute('href'))

        assert presence_checker.is_there_reblogged_post(post_operator, post_id, POST_NOTE)

if __name__ == "__main__":
    unittest.main()