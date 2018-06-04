import unittest
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from logged import LoggedTest

DELAY = 5
SHORT_DELAY = 2

class CommentTest(LoggedTest, unittest.TestCase):

	def add_post(self):
		add_post_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[11]/X.03C/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup")
		add_post_button.click()

		time.sleep(SHORT_DELAY)

		post_text_field = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[9]/android.view.ViewGroup")
		post_text_field.click()

		time.sleep(SHORT_DELAY)

		post_text_field.send_keys("Hi there!")

		time.sleep(SHORT_DELAY)

		submit_post_text_button = self.driver.find_element_by_id("com.facebook.lite:id/inline_textbox_right_button")
		submit_post_text_button.click()

		time.sleep(SHORT_DELAY)

		set_background_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[9]")
		set_background_button.click()

		time.sleep(SHORT_DELAY)

		share_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[12]/android.view.ViewGroup/android.view.ViewGroup")
		share_button.click()

		time.sleep(SHORT_DELAY)

		submit_sharing_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[4]")
		submit_sharing_button.click()

		time.sleep(SHORT_DELAY)

	def add_comment(self):
		add_comment_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[11]/X.03C/android.view.ViewGroup[5]/android.view.ViewGroup[2]/android.view.ViewGroup")
		add_comment_button.click()

		time.sleep(SHORT_DELAY)

		big_text_field = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[8]/android.view.ViewGroup[1]/android.view.ViewGroup")
		big_text_field.click()

		time.sleep(SHORT_DELAY)

		inline_text_field = self.driver.find_element_by_id("com.facebook.lite:id/floating_textbox_edit_text")
		inline_text_field.send_keys("Very nice")

		time.sleep(SHORT_DELAY)

		submit_comment_button = self.driver.find_element_by_id("com.facebook.lite:id/floating_textbox_inline_button")
		submit_comment_button.click()

		time.sleep(SHORT_DELAY)

		news_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup")
		news_button.click()

		time.sleep(SHORT_DELAY)

		added_post_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[11]/X.03C/android.view.ViewGroup[5]/android.view.ViewGroup[2]/android.view.ViewGroup")
		added_post_button.click()

	def test_adding_post(self):
		time.sleep(DELAY)
		self.login('plyuhin.d@mail.ru', 'cassadaga')

		time.sleep(DELAY)
		self.dismiss_login_suggestions()
		
		time.sleep(DELAY)
		self.add_post()

		time.sleep(DELAY)
		self.logout()

	@unittest.skip("skipping")
	def test_adding_comment(self):
		time.sleep(DELAY)
		self.login('plyuhin.d@mail.ru', 'cassadaga')

		time.sleep(DELAY)
		self.dismiss_login_suggestions()
		
		time.sleep(DELAY)
		self.add_comment()

		time.sleep(DELAY)
		self.logout()

if __name__ == '__main__':
	unittest.main()