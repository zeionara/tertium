class PageParser:

    def __init__(self, driver):
        self.driver = driver

    def get_email_input_field(self):
        return self.driver.find_element_by_id("signup_determine_email")

    def get_password_input_field(self):
        return self.driver.find_element_by_id("signup_password")

    def get_error_message(self):
        return self.driver.find_element_by_id("signup_form_errors")

    def get_search_field(self):
        return self.driver.find_element_by_id("search_query")

    def get_search_results_container(self):
        return self.driver.find_element_by_id("search_results_container")

    def get_posts_content(self):
        return self.driver.find_elements_by_class_name("post_content_inner")

    def get_dots(self):
        return self.driver.find_elements_by_class_name("dot")

    def expand_class(self, searched_class):
        return self.driver.find_element_by_class_name(searched_class).get_attribute('class')