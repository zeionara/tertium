class PostOperator:

    def __init__(self, driver):
        self.driver = driver

    def get_posts(self):
        return self.driver.find_elements_by_class_name("post")

    def get_reblogged_posts(self):
        return self.driver.find_elements_by_class_name("reblogged")

    def get_post_id(self, post):
        return str(post.get_attribute('data-post-id'))

    def get_original_post_id(self, post):
    	return str(post.find_element_by_class_name('post-avatar-link').get_attribute('href')).split('/')[-1]

    def get_text_post(self, post_original_title, post_original_body):
        for post in self.get_posts():
            try:
                post_title = post.find_element_by_class_name('post_title')
                post_body = post.find_element_by_class_name('post_body')
            except:
                continue
            if ((post_original_title == post_title.text) and (post_original_body == post_body.text)):
                return post

    def get_control_menu_button(self, post):
        return post.find_element_by_class_name('post_control_menu')

    def get_delete_button(self, post):
        return post.find_element_by_class_name('delete')