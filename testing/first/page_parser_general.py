import time

class PageParserGeneral:

    def get_posted_count(self):
        self.driver.find_element_by_id('account_button').click()
        time.sleep(1)
        try:
            for item in self.driver.find_elements_by_class_name('blog-sub-nav-item-link'):
                if item.find_element_by_class_name('blog-sub-nav-item-label').text == 'Posts':
                    return int(str(item.find_element_by_class_name("blog-sub-nav-item-data").text))
        finally:
            self.driver.find_element_by_id('account_button').click()

    def get_liked_count(self, url):
        self.driver.find_element_by_id('account_button').click()
        time.sleep(1)
        try:
            for item in self.driver.find_elements_by_class_name('popover_menu_item_anchor'):
                if item.get_attribute('href') == url + '/likes':
                    return int(str(item.find_element_by_class_name("popover_item_suffix").text))
        finally:
            self.driver.find_element_by_id('account_button').click()