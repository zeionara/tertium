class ButtonGetterGeneral:

    def get_account_button(self):
        return self.driver.find_element_by_id("account_button")

    def get_account_settings_button(self, url):
        for item in self.driver.find_elements_by_class_name('popover_menu_item_anchor'):
                if item.get_attribute('href') == url + '/settings':
                    return item

    def get_footer_link(self):
        return self.driver.find_element_by_class_name('footer_link')

    def get_help_button(self, url):
        for item in self.driver.find_elements_by_class_name('popover_menu_item_anchor'):
                if item.get_attribute('href') == url + '/help':
                    return item

    def get_activity_button(self):
        return self.driver.find_element_by_id('activity_button')

    def get_messaging_button(self):
        return self.driver.find_element_by_id('messaging_button')

    def get_inbox_button(self):
        return self.driver.find_element_by_id('inbox_button')

    def get_ok_button(self):
        return self.driver.find_element_by_class_name('btn_1')

    def get_posts_button(self):
        for item in self.driver.find_elements_by_class_name('blog-sub-nav-item-link'):
                if 'Posts' in item.text:
                    return item

    def get_post_settings_button(self):
        return self.driver.find_element_by_class_name('post-settings')

    def get_discover_button(self):
        return self.driver.find_element_by_id('discover_button')