import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from subprocess import call

from utils import PostOperator, PresenceChecker, ButtonGetter

CHROME_DRIVER_LOCATION = './chromedriver'
URL = "https://www.tumblr.com/"

INITIAL_NUMBER_OF_POSTS_TO_SHOW = 38

FOLLOWING_INDEX = 3
FIRST_POST_INDEX = 2

SESSION_URL = os.environ['SESSION_URL']
SESSION_ID = os.environ['SESSION_ID']

INBOX_PATH = '/inbox'

class AccountTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(command_executor = SESSION_URL, desired_capabilities={})
        self.driver.session_id = SESSION_ID
        print('called:', call(['xdotool','getwindowfocus','windowkill']))
        self.driver.get(URL + "/dashboard")

    def tearDown(self):
        pass
        #self.driver.close()

    def get_language_selector(self):
        return self.driver.find_element_by_id('user_language')

@unittest.skip("skipping")
class SettingsTest(AccountTest):

    def test_changing_settings_succeeded(self):
        driver = self.driver
        #self.login()

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
        #self.login()

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
        #self.login()

        button_getter = ButtonGetter(driver)
        presence_checker = PresenceChecker(driver)
        post_operator = PostOperator(driver)

        self.assertFalse(presence_checker.is_there_activity_popover())

        button_getter.get_activity_button().click()
        
        time.sleep(1)

        self.assertTrue(presence_checker.is_there_activity_popover())

@unittest.skip("skipping")
class MessagingTest(AccountTest):

    def test_messaging_succeeded(self):
        driver = self.driver
        #self.login()

        button_getter = ButtonGetter(driver)
        presence_checker = PresenceChecker(driver)
        post_operator = PostOperator(driver)

        self.assertFalse(presence_checker.is_there_messaging_inbox())

        button_getter.get_messaging_button().click()
        
        time.sleep(1)

        self.assertTrue(presence_checker.is_there_messaging_inbox())

#@unittest.skip("skipping")
class InboxTest(AccountTest):

    def test_inbox_redirect_succeeded(self):
        driver = self.driver

        button_getter = ButtonGetter(driver)
        presence_checker = PresenceChecker(driver)
        post_operator = PostOperator(driver)

        button_getter.get_inbox_button().click()

        time.sleep(1)

        self.assertTrue(INBOX_PATH in driver.current_url)

if __name__ == "__main__":
    unittest.main()