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

    def type_and_confirm_language(self, language):
        language_selector = self.page_parser.get_language_selector()
        language_selector.send_keys(language)
        language_selector.send_keys(Keys.RETURN)

    def type_language(self, language):
        language_selector = self.page_parser.get_language_selector()
        language_selector.send_keys(language)

    def confirm_language(self):
        language_selector = self.page_parser.get_language_selector()
        language_selector.send_keys(Keys.RETURN)

    def click_delete_account_button(self):
        self.button_getter.get_delete_account_button().click()