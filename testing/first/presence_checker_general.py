class PresenceCheckerGeneral:

	def __init__(self, driver):
		self.driver = driver

	def is_there_item_with_class(self, searched_class):
		try:
			self.driver.find_element_by_class_name(searched_class)
		except:
			return False
		return True

	def is_there_glass_container(self):
		return self.is_there_item_with_class("ui_peepr_glass")

	def is_there_follower_container(self):
		return self.is_there_item_with_class("peepr-drawer-container")

	def is_there_post(self, post_operator, post_id):
		for post in post_operator.get_posts():
			if post_operator.get_post_id(post) == post_id:
				return True
		return False

	def is_there_tab_with_url_part(self, title_part):
		current_window_handle = self.driver.current_window_handle
		try:
			for handle in self.driver.window_handles:
				self.driver.switch_to_window(handle)
				if title_part in self.driver.current_url:
					return True
		finally:
			self.driver.switch_to_window(current_window_handle)

		return False

	def is_there_drawer_container(self):
		return self.is_there_item_with_class("drawer")

	def is_there_post_modal_container(self):
		return self.is_there_item_with_class('post-form-modal-content')

   	def is_there_post_settings_dropdown(self):
		return self.is_there_item_with_class('popover--post-settings-dropdown')

	def is_there_reblogged_post(self, post_operator, post_id, post_note):
		for post in post_operator.get_reblogged_posts():
			if (post_operator.get_original_post_id(post) == str(post_id)):
			 	if (post_note in post.text):
					return True
		return False


