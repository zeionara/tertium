import unittest
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from logged import LoggedTest

DELAY = 5
SHORT_DELAY = 2

class PageTest(LoggedTest, unittest.TestCase):

	def create_page(self):
		menu_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup")
		menu_button.click()

		time.sleep(SHORT_DELAY)

		skip_friends_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup")
		skip_friends_button.click()

		time.sleep(SHORT_DELAY)

		menu_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[6]/android.view.ViewGroup")
		menu_button.click()

		time.sleep(SHORT_DELAY)

		pages_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[9]")#android.view.ViewGroup[7]")
		pages_button.click()

		time.sleep(SHORT_DELAY)

		create_page_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[5]/X.03C/android.view.ViewGroup[6]/android.view.ViewGroup[5]")#android.view.ViewGroup[3]")
		create_page_button.click()

		time.sleep(SHORT_DELAY)

		page_name_text_field = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[4]")
		page_name_text_field.click()

		time.sleep(SHORT_DELAY)

		page_name_text_field.send_keys("Cogitare")

		time.sleep(SHORT_DELAY)

		categories_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[6]")
		categories_button.click()

		time.sleep(SHORT_DELAY)

		categories_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[6]")
		categories_button.click()

		time.sleep(SHORT_DELAY)

		other_category_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[10]")
		other_category_button.click()

		time.sleep(SHORT_DELAY)

		other_subcategory_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[7]")
		other_subcategory_button.click()

		time.sleep(SHORT_DELAY)

		submit_page_creation_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[8]/android.view.ViewGroup")
		submit_page_creation_button.click()

		time.sleep(SHORT_DELAY)

	def test_page_creation(self):
		time.sleep(DELAY)
		self.login('plyuhin.d@mail.ru', 'cassadaga')

		time.sleep(DELAY)
		self.dismiss_login_suggestions()
		
		time.sleep(DELAY)
		self.create_page()

		time.sleep(DELAY)
		self.logout()

if __name__ == '__main__':
	unittest.main()