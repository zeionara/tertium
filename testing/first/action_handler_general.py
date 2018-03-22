from selenium.webdriver.common.keys import Keys

class ActionHandlerGeneral:

    def click_inbox_button(self):
        self.button_getter.get_inbox_button().click()

    def click_messaging_button(self):
        self.button_getter.get_messaging_button().click()

    def click_activity_button(self):
        self.button_getter.get_activity_button().click()

    def click_account_button(self):
        self.button_getter.get_account_button().click()

    def click_help_button(self, url):
        self.button_getter.get_help_button(url).click()

    def click_account_settings_button(self, url):
        self.button_getter.get_account_settings_button(url).click()

    def click_footer_link(self):
        self.button_getter.get_footer_link().click()

    def switch(self, switcher):
        switcher.send_keys(Keys.SPACE)

    def type_search_query(self, query):
        search_field = self.page_parser.get_search_field()
        search_field.send_keys(query)

    def confirm_search_query(self):
        self.page_parser.get_search_field().send_keys(Keys.RETURN)