# -*- coding: utf-8 -*-

import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

from utils import PostOperator, PresenceChecker, ButtonGetter

CHROME_DRIVER_LOCATION = './chromedriver'
URL = "https://www.tumblr.com/"

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
POST_NOTE = os.environ['POST_NOTE']

INITIAL_NUMBER_OF_POSTS_TO_SHOW = 38

FOLLOWING_INDEX = 3
FIRST_POST_INDEX = 2


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_LOCATION)
        self.driver.get(URL + "/login")

    def login(self):
        driver = self.driver
        
        email_field = self.driver.find_element_by_id("signup_determine_email")
        email_field.send_keys(EMAIL)
        email_field.send_keys(Keys.RETURN)

        time.sleep(2)

        password_field = self.driver.find_element_by_id("signup_password")
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.RETURN)

        assert "Sign up" not in driver.title

    def tearDown(self):
        self.driver.close()

    def get_dismiss_titles(self):
        return self.driver.find_elements_by_class_name("tumblelog_title");

    def get_following(self):
        following = []
        for item in self.driver.find_elements_by_class_name("name-link"):
            following.append(item.text)
        return following

    def get_follower_links(self):
        return self.driver.find_elements_by_class_name("follow_list_item_blog")

    def get_liked_count(self):
        self.driver.find_element_by_id('account_button').click()
        time.sleep(1)
        try:
            for item in self.driver.find_elements_by_class_name('popover_menu_item_anchor'):
                if item.get_attribute('href') == URL + 'likes':
                    return item.find_element_by_class_name("popover_item_suffix").text
        finally:
            self.driver.find_element_by_id('account_button').click()

    def get_posted_count(self):
        self.driver.find_element_by_id('account_button').click()
        time.sleep(1)
        try:
            for item in self.driver.find_elements_by_class_name('blog-sub-nav-item-link'):
                if item.find_element_by_class_name('blog-sub-nav-item-label').text == 'Posts':
                    return int(str(item.find_element_by_class_name("blog-sub-nav-item-data").text))
        finally:
            self.driver.find_element_by_id('account_button').click()

    def get_reblog_text_field(self):
        return self.driver.find_element_by_class_name('editor-richtext')

    def get_post_avatar_link(self):
        return self.driver.find_element_by_class_name('post_avatar_link')

    ############

    def get_language_selector(self):
        return self.driver.find_element_by_id('user_language')

@unittest.skip("skipping")
class SettingsTest(AccountTest):

    def test_changing_settings_succeeded(self):
        driver = self.driver
        self.login()

        button_getter = ButtonGetter(driver)
        presence_checker = PresenceChecker(driver)
        post_operator = PostOperator(driver)

        button_getter.get_account_button().click()
        time.sleep(1)

        button_getter.get_account_settings_button(URL).click()

        language_selector = self.get_language_selector()

        language_selector.send_keys('Deutsch')
        language_selector.send_keys(Keys.RETURN)

        time.sleep(3)

        assert 'Account-Einstellungen' in driver.title

        language_selector = self.get_language_selector()

        language_selector.send_keys('English')

        time.sleep(1)

        self.get_language_selector().send_keys('English')

        time.sleep(1)

        self.get_language_selector().send_keys(Keys.SPACE)

        time.sleep(3)

        assert 'Account Settings' in driver.title

        button_getter.get_delete_account_button().click()

        time.sleep(2)

        assert 'delete' in driver.current_url

        button_getter.get_footer_link().click()

        time.sleep(2)

        button_getter.get_dashboard_settings_button().click()

        assert 'dashboard' in driver.current_url

        button_getter.get_notifications_settings_button().click()

        assert 'notifications' in driver.current_url

        switcher = button_getter.get_notifications_switcher()

        switcher.send_keys(Keys.SPACE)
        time.sleep(1)
        switcher.send_keys(Keys.SPACE)

        button_getter.get_apps_settings_button().click()

        assert 'apps' in driver.current_url

        button_getter.get_android_button().click()
        button_getter.get_ios_button().click()

        self.assertTrue(presence_checker.is_there_tab_with_url_part('itunes.apple.com'))
        self.assertTrue(presence_checker.is_there_tab_with_url_part('play.google.com'))

        button_getter.get_labs_settings_button().click()

        assert 'labs' in driver.current_url

        labs_switcher = button_getter.get_labs_switcher()

        labs_switcher.send_keys(Keys.SPACE)
        time.sleep(1)
        labs_switcher.send_keys(Keys.SPACE)

@unittest.skip("skipping")
class HelpTest(AccountTest):

    def test_calling_help_succeeded(self):
        driver = self.driver
        self.login()

        button_getter = ButtonGetter(driver)
        presence_checker = PresenceChecker(driver)
        post_operator = PostOperator(driver)

        button_getter.get_account_button().click()
        time.sleep(1)

        button_getter.get_help_button(URL).click()

        time.sleep(3)

        assert 'tumblr.zendesk.com' in self.driver.current_url

@unittest.skip("skipping")
class ActivityTest(AccountTest):

    def test_calling_activity_succeeded(self):
        driver = self.driver
        self.login()

        button_getter = ButtonGetter(driver)
        presence_checker = PresenceChecker(driver)
        post_operator = PostOperator(driver)

        self.assertFalse(presence_checker.is_there_activity_popover())

        button_getter.get_activity_button().click()
        
        time.sleep(1)

        self.assertTrue(presence_checker.is_there_activity_popover())

#@unittest.skip("skipping")
class MessagingTest(AccountTest):

    def test_messaging_succeeded(self):
        driver = self.driver
        self.login()

        button_getter = ButtonGetter(driver)
        presence_checker = PresenceChecker(driver)
        post_operator = PostOperator(driver)

        self.assertFalse(presence_checker.is_there_messaging_inbox())

        button_getter.get_messaging_button().click()
        
        time.sleep(1)

        self.assertTrue(presence_checker.is_there_messaging_inbox())




if __name__ == "__main__":
    unittest.main()