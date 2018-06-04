import unittest
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from logged import LoggedTest

DELAY = 5
SHORT_DELAY = 2

class MessageTest(LoggedTest, unittest.TestCase):

	def send_message(self):
		messages_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[3]/android.view.ViewGroup")
		messages_button.click()

		time.sleep(SHORT_DELAY)

		conversation_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[10]/X.03C/android.view.ViewGroup[3]")
		conversation_button.click()

		time.sleep(SHORT_DELAY)

		text_field = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup")
		text_field.click()
		time.sleep(SHORT_DELAY)
		text_field.send_keys("Hello")

		time.sleep(SHORT_DELAY)

		send_button = self.driver.find_element_by_id("com.facebook.lite:id/floating_textbox_right_button")
		send_button.click()

		time.sleep(SHORT_DELAY)

		back_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup")
		back_button.click()

		time.sleep(SHORT_DELAY)

		news_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup")
		news_button.click()

		time.sleep(SHORT_DELAY)

	def test_sending_message(self):
		time.sleep(DELAY)
		self.login('plyuhin.d@mail.ru', 'cassadaga')

		time.sleep(DELAY)
		self.dismiss_login_suggestions()
		
		time.sleep(DELAY)
		self.send_message()

		time.sleep(DELAY)
		self.logout()

if __name__ == '__main__':
	unittest.main()