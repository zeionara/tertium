import sys
import os
from os import path

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from presence_checker_general import PresenceCheckerGeneral

class PresenceChecker(PresenceCheckerGeneral):

	def __init__(self, driver):
		self.driver = driver

	def is_there_messaging_inbox(self):
		return self.is_there_item_with_class('messaging-inbox')

	def is_there_activity_popover(self):
		return self.is_there_item_with_class('popover--activity-popover')