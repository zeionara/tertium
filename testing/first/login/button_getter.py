import sys
import os
from os import path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from button_getter_general import ButtonGetterGeneral

class ButtonGetter(ButtonGetterGeneral):

    def __init__(self, driver):
        self.driver = driver

    def get_signup_login_button(self):
        return self.driver.find_element_by_id("signup_login_button")

    def get_logout_button(self):
        return self.driver.find_element_by_id('logout_button')