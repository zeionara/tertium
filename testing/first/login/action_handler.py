from selenium.webdriver.common.keys import Keys
import time
import sys
import os
from os import path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from page_parser import PageParser
from button_getter import ButtonGetter
from action_handler_general import ActionHandlerGeneral

class ActionHandler(ActionHandlerGeneral):

    def __init__(self, driver):
        self.page_parser = PageParser(driver)
        self.button_getter = ButtonGetter(driver)

    def type_and_confirm_email(self, email):
        email_field = self.page_parser.get_email_input_field()
        email_field.send_keys(email)
        email_field.send_keys(Keys.RETURN)

    def type_and_confirm_password(self, password):
        password_field = self.page_parser.get_password_input_field()
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

    def click_login_button(self):
        signup_button = self.button_getter.get_signup_login_button()
        signup_button.click()

    def assert_active_section(self, sections, section_index):
        active_section_name = sections[section_index]
        for section_name in sections:
            assert (section_name + '-section' == active_section_name + '-section') == \
                ('active' in self.page_parser.expand_class(section_name + '-section'))

    def logout(self):
        self.button_getter.get_account_button().click()
        time.sleep(0.5)
        self.button_getter.get_logout_button().click()
        time.sleep(0.5)
        self.button_getter.get_ok_button().click()