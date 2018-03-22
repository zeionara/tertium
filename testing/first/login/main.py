import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from subprocess import call

from button_getter import ButtonGetter
from page_parser import PageParser
from action_handler import ActionHandler

CHROME_DRIVER_LOCATION = './chromedriver'
URL = "https://www.tumblr.com/"

SESSION_URL = os.environ['SESSION_URL']
SESSION_ID = os.environ['SESSION_ID']

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']

EMAIL_WRONG_APPENDIX = 'aaaaaaaaa'
PASSWORD_WRONG_APPENDIX = 'bbbbbbbbb'
SEARCH_QEURY = 'test'

SECTIONS = ['login', 'about', 'blogs', 'dashboard', 'create', 'welcome']
MIN_NUMBER_OF_POSTS = 10

class LoginPageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Remote(command_executor = SESSION_URL, desired_capabilities={})
        self.driver.session_id = SESSION_ID

        call(['xdotool','getwindowfocus','windowkill'])
        
        self.driver.get(URL)

    def tearDown(self):
        pass

#@unittest.skip("skipping")
class LoginSuccess(LoginPageTest):

    def test_login_succeeded(self):
        driver = self.driver

        action_handler = ActionHandler(driver)
        
        assert "Tumblr" in driver.title
        
        action_handler.click_login_button()
        action_handler.type_and_confirm_email(EMAIL)

        time.sleep(2)

        action_handler.type_and_confirm_password(PASSWORD)

        assert "Log in" not in driver.title

        action_handler.logout()

        time.sleep(2)

#@unittest.skip("skipping")
class LoginEmailFail(LoginPageTest):

    def test_login_failed_with_wrong_email(self):
        driver = self.driver

        action_handler = ActionHandler(driver)
        page_parser = PageParser(driver)

        assert not page_parser.get_error_message().is_displayed()
        assert "Tumblr" in driver.title
        
        action_handler.click_login_button()
        action_handler.type_and_confirm_email(EMAIL + EMAIL_WRONG_APPENDIX)

        time.sleep(2)

        assert not page_parser.get_password_input_field().is_displayed()
        assert page_parser.get_error_message().is_displayed()

#@unittest.skip("skipping")
class LoginPasswordFail(LoginPageTest):

    def test_login_failed_with_wrong_password(self):
        driver = self.driver

        action_handler = ActionHandler(driver)
        page_parser = PageParser(driver)

        assert not page_parser.get_error_message().is_displayed()
        assert "Tumblr" in driver.title
        
        action_handler.click_login_button()
        action_handler.type_and_confirm_email(EMAIL)

        time.sleep(2)

        action_handler.type_and_confirm_password(PASSWORD + PASSWORD_WRONG_APPENDIX)

        time.sleep(5)

        assert "Log in" in driver.title
        assert page_parser.get_error_message().is_displayed()

#@unittest.skip("skipping")
class SearchSuccess(LoginPageTest):

    def test_search_success(self):
        driver = self.driver

        action_handler = ActionHandler(driver)
        page_parser = PageParser(driver)

        assert not page_parser.get_search_results_container().is_displayed()
        
        action_handler.type_search_query(SEARCH_QEURY)

        time.sleep(1)

        assert page_parser.get_search_results_container().is_displayed()
        
        action_handler.confirm_search_query()

        assert len(page_parser.get_posts_content()) >= MIN_NUMBER_OF_POSTS

#@unittest.skip("skipping")
class ScrollWork(LoginPageTest):

    def test_scroll_works(self):
        driver = self.driver

        action_handler = ActionHandler(driver)
        page_parser = PageParser(driver)

        for section_index in range(len(SECTIONS)):
            page_parser.get_dots()[section_index].click()
            time.sleep(3)
            action_handler.assert_active_section(SECTIONS, section_index)
        
if __name__ == "__main__":
    unittest.main()