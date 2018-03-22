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
        self.driver = driver

    def click_confirm_post(self):
        self.driver.execute_script("document.getElementsByClassName('create_post_button')[0].click()")