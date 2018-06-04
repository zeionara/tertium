import unittest
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from logged import LoggedTest

DELAY = 5
SHORT_DELAY = 2

class LoginTest(LoggedTest, unittest.TestCase):

	def confirm_error(self):
		error_ack_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup")
		assert error_ack_button
		error_ack_button.click()

	#@unittest.skip("skipping")
	def test_invalid_email(self):
		time.sleep(DELAY)

		self.login('hello', 'hello')
		self.confirm_error()

	#@unittest.skip("skipping")
	def test_invalid_password(self):
		time.sleep(DELAY)

		self.login('hello@gmail.com', 'hello')
		self.confirm_error()

	def test_valid_password(self):
		time.sleep(DELAY)
		self.login('plyuhin.d@mail.ru', 'cassadaga')

		time.sleep(DELAY)
		self.dismiss_login_suggestions()
		
		time.sleep(DELAY)
		self.logout()

if __name__ == '__main__':
	unittest.main()