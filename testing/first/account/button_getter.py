import sys
import os
from os import path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from button_getter_general import ButtonGetterGeneral

class ButtonGetter(ButtonGetterGeneral):

    def __init__(self, driver):
        self.driver = driver

    def get_delete_account_button(self):
        return self.driver.find_element_by_class_name('delete')

    def get_dashboard_settings_button(self):
        return self.driver.find_element_by_class_name('controls_item_dashboard')

    def get_notifications_settings_button(self):
        return self.driver.find_element_by_class_name('controls_item_notifications')

    def get_notifications_switcher(self):
        return self.driver.find_element_by_id('user_permit_marketing_emails')

    def get_apps_settings_button(self):
        return self.driver.find_element_by_class_name('controls_item_apps')

    def get_android_button(self):
        return self.driver.find_element_by_id('app_android')

    def get_ios_button(self):
        return self.driver.find_element_by_id('app_iphone')

    def get_labs_settings_button(self):
        return self.driver.find_element_by_class_name('controls_item_labs')

    def get_labs_switcher(self):
        return self.driver.find_element_by_id('labs_user_opt_in')