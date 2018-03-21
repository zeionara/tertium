import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from subprocess import call

CHROME_DRIVER_LOCATION = './chromedriver'
URL = "https://www.tumblr.com/"

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']

SESSION_URL = os.environ['SESSION_URL']
SESSION_ID = os.environ['SESSION_ID']

INITIAL_NUMBER_OF_POSTS_TO_SHOW = 38

class LoginPageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Remote(command_executor = SESSION_URL, desired_capabilities={})
        self.driver.session_id = SESSION_ID
        print('called:', call(['xdotool','getwindowfocus','windowkill']))
        self.driver.get(URL)

    def tearDown(self):
        pass
        #self.driver.close()

    def get_signup_login_button(self):
        return self.driver.find_element_by_id("signup_login_button")

    def get_email_input_field(self):
        return self.driver.find_element_by_id("signup_determine_email")

    def get_password_input_field(self):
        return self.driver.find_element_by_id("signup_password")

    def get_error_message(self):
        return self.driver.find_element_by_id("signup_form_errors")

    def get_search_field(self):
        return self.driver.find_element_by_id("search_query")

    def get_search_results_container(self):
        return self.driver.find_element_by_id("search_results_container")

    def get_posts_content(self):
        return self.driver.find_elements_by_class_name("post_content_inner")

    def get_dots(self):
        return self.driver.find_elements_by_class_name("dot")

#@unittest.skip("skipping")
class LoginSuccess(LoginPageTest):

    def test_login_succeeded(self):
        driver = self.driver
        
        self.assertIn("Tumblr", driver.title)
        
        signup_button = self.get_signup_login_button()
        signup_button.click()
        
        email_field = self.get_email_input_field()
        email_field.send_keys(EMAIL)
        email_field.send_keys(Keys.RETURN)

        time.sleep(2)

        password_field = self.get_password_input_field()
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.RETURN)

        assert "Sign up" not in driver.title

#@unittest.skip("skipping")
class LoginEmailFail(LoginPageTest):

    def test_login_failed_with_wrong_email(self):
        driver = self.driver

        error_message = self.get_error_message()
        self.assertFalse(error_message.is_displayed())

        self.assertIn("Tumblr", driver.title)
        
        signup_button = self.get_signup_login_button()
        signup_button.click()
        
        email_field = self.get_email_input_field()
        email_field.send_keys(EMAIL+'dkowkdoks')
        email_field.send_keys(Keys.RETURN)

        time.sleep(2)

        password_field = self.get_password_input_field()

        self.assertFalse(password_field.is_displayed())

        error_message = self.get_error_message()
        self.assertTrue(error_message.is_displayed())

#@unittest.skip("skipping")
class LoginPasswordFail(LoginPageTest):

    def test_login_failed_with_wrong_password(self):
        driver = self.driver

        error_message = self.get_error_message()
        self.assertFalse(error_message.is_displayed())
        
        self.assertIn("Tumblr", driver.title)
        
        signup_button = self.get_signup_login_button()
        signup_button.click()
        
        email_field = self.get_email_input_field()
        email_field.send_keys(EMAIL)
        email_field.send_keys(Keys.RETURN)

        time.sleep(2)

        password_field = self.get_password_input_field()
        password_field.send_keys(PASSWORD+'----------')
        password_field.send_keys(Keys.RETURN)

        time.sleep(5)

        assert "Log in" in driver.title

        error_message = self.get_error_message()
        self.assertTrue(error_message.is_displayed())

#@unittest.skip("skipping")
class SearchSuccess(LoginPageTest):

    def test_search_success(self):
        driver = self.driver
        search_results_container = self.get_search_results_container()

        self.assertFalse(search_results_container.is_displayed())
        
        search_field = self.get_search_field()
        search_field.send_keys('test')

        time.sleep(1)

        self.assertTrue(search_results_container.is_displayed())
        search_field.send_keys(Keys.RETURN)

        self.assertEquals(len(self.get_posts_content()), INITIAL_NUMBER_OF_POSTS_TO_SHOW)


class ScrollWork(LoginPageTest):

    def test_scroll_works(self):
        driver = self.driver

        self.assertTrue('active' in driver.find_element_by_class_name("login-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("about-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("blogs-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("dashboard-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("create-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("welcome-section").get_attribute('class'))
        
        self.get_dots()[1].click()
        time.sleep(3)

        self.assertFalse('active' in driver.find_element_by_class_name("login-section").get_attribute('class'))
        self.assertTrue('active' in driver.find_element_by_class_name("about-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("blogs-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("dashboard-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("create-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("welcome-section").get_attribute('class'))

        self.get_dots()[2].click()
        time.sleep(3)

        self.assertFalse('active' in driver.find_element_by_class_name("login-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("about-section").get_attribute('class'))
        self.assertTrue('active' in driver.find_element_by_class_name("blogs-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("dashboard-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("create-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("welcome-section").get_attribute('class'))

        self.get_dots()[3].click()
        time.sleep(3)

        self.assertFalse('active' in driver.find_element_by_class_name("login-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("about-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("blogs-section").get_attribute('class'))
        self.assertTrue('active' in driver.find_element_by_class_name("dashboard-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("create-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("welcome-section").get_attribute('class'))

        self.get_dots()[4].click()
        time.sleep(3)

        self.assertFalse('active' in driver.find_element_by_class_name("login-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("about-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("blogs-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("dashboard-section").get_attribute('class'))
        self.assertTrue('active' in driver.find_element_by_class_name("create-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("welcome-section").get_attribute('class'))

        self.get_dots()[5].click()
        time.sleep(3)

        self.assertFalse('active' in driver.find_element_by_class_name("login-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("about-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("blogs-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("dashboard-section").get_attribute('class'))
        self.assertFalse('active' in driver.find_element_by_class_name("create-section").get_attribute('class'))
        self.assertTrue('active' in driver.find_element_by_class_name("welcome-section").get_attribute('class'))
        
if __name__ == "__main__":
    unittest.main()