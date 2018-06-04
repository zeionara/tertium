import unittest
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

DELAY = 8
SHORT_DELAY = 3

class LoggedTest(unittest.TestCase):

	def setUp(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '8.0'
		desired_caps['deviceName'] = 'Zyra'
		desired_caps['app'] = 'C:/Users/prote/Documents/appium/com.facebook.lite_96.0.0.7.216-110083574_minAPI9(x86)(nodpi)_apkmirror.com.apk'

		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

	def login(self, login, password):
		password_field = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[1]/android.view.ViewGroup[4]")
		password_field.send_keys(password)

		login_field = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[1]/android.view.ViewGroup[2]")
		login_field.send_keys(login)
		
		login_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup")
		login_button.click()

		time.sleep(DELAY)

	def dismiss_login_suggestions(self):
		not_save_login_data_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[4]/android.view.ViewGroup")
		not_save_login_data_button.click()

		time.sleep(SHORT_DELAY)

		not_add_friends_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[4]/android.view.ViewGroup")
		not_add_friends_button.click()

		time.sleep(SHORT_DELAY)

	def logout(self):
		#open preferences and go to bottom
		TouchAction(self.driver).tap(x=702, y=102).perform()
		time.sleep(SHORT_DELAY)
		dismiss_adding_friends_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup")
		dismiss_adding_friends_button.click()
		time.sleep(SHORT_DELAY)
		TouchAction(self.driver).tap(x=702, y=102).perform()
		time.sleep(SHORT_DELAY)
		TouchAction(self.driver).press(x=400, y=1000).move_to(x=400, y=400).release().perform()
		time.sleep(SHORT_DELAY)
		TouchAction(self.driver).press(x=400, y=1000).move_to(x=400, y=400).release().perform()
		time.sleep(SHORT_DELAY)
		TouchAction(self.driver).press(x=400, y=1000).move_to(x=400, y=400).release().perform()
		
		logout_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[10]")
		logout_button.click()

		time.sleep(SHORT_DELAY)

		not_save_password_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup")
		not_save_password_button.click()

		time.sleep(SHORT_DELAY)

		#press on three dots right to the user's picture
		TouchAction(self.driver).tap(x=704, y=267).perform()

		time.sleep(SHORT_DELAY)

		delete_account_from_device_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[5]/android.view.ViewGroup[2]")
		delete_account_from_device_button.click()

		time.sleep(SHORT_DELAY)

		submit_deleting_account_from_device_button = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.ViewGroup")
		submit_deleting_account_from_device_button.click()