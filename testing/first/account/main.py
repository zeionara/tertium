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

from button_getter import ButtonGetter
from page_parser import PageParser
from action_handler import ActionHandler
from presence_checker import PresenceChecker
from post_operator import PostOperator

CHROME_DRIVER_LOCATION = './chromedriver'
URL = "https://www.tumblr.com"

INITIAL_NUMBER_OF_POSTS_TO_SHOW = 38

FOLLOWING_INDEX = 3
FIRST_POST_INDEX = 2

SESSION_URL = os.environ['SESSION_URL']
SESSION_ID = os.environ['SESSION_ID']

INBOX_PATH = '/inbox'
HELP_DOMAIN = 'tumblr.zendesk.com'

class AccountTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor = SESSION_URL, desired_capabilities={})
        self.driver.session_id = SESSION_ID

        call(['xdotool','getwindowfocus','windowkill'])
        
        self.driver.get(URL + "/dashboard")

    def tearDown(self):
        pass

#@unittest.skip("skipping")
class SettingsTest(AccountTest):

    def test_changing_settings_succeeded(self):
        driver = self.driver

        button_getter = ButtonGetter(driver)
        presence_checker = PresenceChecker(driver)
        post_operator = PostOperator(driver)
        action_handler = ActionHandler(driver)
        page_parser = PageParser(driver)

        action_handler.click_account_button()
        
        time.sleep(1)

        action_handler.click_account_settings_button(URL)
        action_handler.type_and_confirm_language('Deutsch')

        time.sleep(3)

        assert 'Account-Einstellungen' in driver.title

        action_handler.type_and_confirm_language('English')

        time.sleep(3)

        assert 'Account Settings' in driver.title

        action_handler.click_delete_account_button()

        time.sleep(2)

        assert 'delete' in driver.current_url

        action_handler.click_footer_link()

        time.sleep(2)

        button_getter.get_dashboard_settings_button().click()

        assert 'dashboard' in driver.current_url

        button_getter.get_notifications_settings_button().click()

        assert 'notifications' in driver.current_url

        switcher = button_getter.get_notifications_switcher()

        action_handler.switch(switcher)
        time.sleep(1)
        action_handler.switch(switcher)

        button_getter.get_apps_settings_button().click()

        assert 'apps' in driver.current_url

        button_getter.get_android_button().click()
        button_getter.get_ios_button().click()

        assert presence_checker.is_there_tab_with_url_part('itunes.apple.com')
        assert presence_checker.is_there_tab_with_url_part('play.google.com')

        button_getter.get_labs_settings_button().click()

        assert 'labs' in driver.current_url

        labs_switcher = button_getter.get_labs_switcher()

        action_handler.switch(labs_switcher)
        time.sleep(1)
        action_handler.switch(labs_switcher)

#@unittest.skip("skipping")
class HelpTest(AccountTest):

    def test_calling_help_succeeded(self):
        driver = self.driver

        action_handler = ActionHandler(driver)

        action_handler.click_account_button()

        time.sleep(1)

        action_handler.click_help_button(URL)

        time.sleep(3)

        assert HELP_DOMAIN in self.driver.current_url

#@unittest.skip("skipping")
class ActivityTest(AccountTest):

    def test_calling_activity_succeeded(self):
        driver = self.driver

        action_handler = ActionHandler(driver)
        presence_checker = PresenceChecker(driver)

        assert not presence_checker.is_there_activity_popover()

        action_handler.click_activity_button()

        assert presence_checker.is_there_activity_popover()

#@unittest.skip("skipping")
class MessagingTest(AccountTest):

    def test_messaging_succeeded(self):
        driver = self.driver

        action_handler = ActionHandler(driver)
        presence_checker = PresenceChecker(driver)

        assert not presence_checker.is_there_messaging_inbox()

        action_handler.click_messaging_button()

        assert presence_checker.is_there_messaging_inbox()

#@unittest.skip("skipping")
class InboxTest(AccountTest):

    def test_inbox_redirect_succeeded(self):
        driver = self.driver

        action_handler = ActionHandler(driver)

        action_handler.click_inbox_button()
        assert INBOX_PATH in driver.current_url

if __name__ == "__main__":
    unittest.main()