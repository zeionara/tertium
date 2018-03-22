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

class PresenceChecker:

    def __init__(self, driver):
        self.driver = driver

    def is_there_item_with_class(self, searched_class):
        try:
            self.driver.find_element_by_class_name(searched_class)
        except:
            return False
        return True

    def is_there_follower_container(self):
        return self.is_there_item_with_class("peepr-drawer-container")

    def is_there_drawer_container(self):
        return self.is_there_item_with_class("drawer")

    def is_there_glass_container(self):
        return self.is_there_item_with_class("ui_peepr_glass")

    def is_there_post(self, post_operator, post_id):
        for post in post_operator.get_posts():
            if post_operator.get_post_id(post) == post_id:
            	print('post text:', post.text)
                return True
        return False

    def is_there_reblogged_post(self, post_operator, post_id, post_note):
        for post in post_operator.get_reblogged_posts():
            if (post_operator.get_original_post_id(post) == str(post_id)):
             	if (post_note in post.text):
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

    def is_there_tab_with_title_part(self, title_part):
        current_window_handle = self.driver.current_window_handle
        try:
            for handle in self.driver.window_handles:
                self.driver.switch_to_window(handle)
                print('title:',str(self.driver.title))
                print(title_part, ' in ', str(self.driver.title))
                if title_part in str(self.driver.title):
                    return True
        finally:
            self.driver.switch_to_window(current_window_handle)

        return False

    def is_there_post_modal_container(self):
    	return self.is_there_item_with_class('post-form-modal-content')

    def is_there_post_settings_dropdown(self):
    	return self.is_there_item_with_class('popover--post-settings-dropdown')

    def is_there_post_inside_drawer(self, post_operator, post_id):
    	for post in self.driver.find_elements_by_class_name('drawer').find_elements_by_class_name('post'):
    		if post_operator.get_post_id(post) == post_id:
    			print(post.text)

    def is_there_activity_popover(self):
        return self.is_there_item_with_class('popover--activity-popover')

    def is_there_messaging_inbox(self):
        return self.is_there_item_with_class('messaging-inbox')

class ButtonGetter:

    def __init__(self, driver):
        self.driver = driver

    def get_follow_buttons(self):
        return self.driver.find_elements_by_class_name("plus-follow-button")

    def get_dismiss_buttons(self):
        return self.driver.find_elements_by_class_name("dismiss")

    def get_account_button(self):
        return self.driver.find_element_by_id("account_button")

    def get_unfollow_button(self, follower):
        return self.driver.find_element_by_id("unfollow_button_"+follower)

    def get_like_button(self, post):
        return post.find_element_by_class_name("like")

    def get_like_button_by_post_id(self, post_operator, post_id):
        for post in post_operator.get_posts():
            if post_operator.get_post_id(post) == post_id:
                return self.get_like_button(post)

    def get_permalink_button(self):
        return self.driver.find_element_by_class_name('messaging-share-post-external-network')

    def get_embed_button(self):
        return self.driver.find_element_by_class_name('network--embed')

    def get_report_button(self):
        return self.driver.find_element_by_class_name('network--flag')

    def get_share_button(self, post):
        return post.find_element_by_class_name('share')

    def get_reblog_button(self, post):
    	return post.find_element_by_class_name('reblog')

    def get_reblog_applying_button(self):
    	return self.driver.find_element_by_class_name('create_post_button')

    def get_post_settings_button(self):
    	return self.driver.find_element_by_class_name('post-settings')

    def get_account_button(self):
        return self.driver.find_element_by_id('account_button')

    def get_activity_button(self):
        return self.driver.find_element_by_id('activity_button')

    def get_account_settings_button(self, url):
        for item in self.driver.find_elements_by_class_name('popover_menu_item_anchor'):
                if item.get_attribute('href') == url + 'settings':
                    return item

    def get_help_button(self, url):
        for item in self.driver.find_elements_by_class_name('popover_menu_item_anchor'):
                if item.get_attribute('href') == url + 'help':
                    return item

    def get_dashboard_settings_button(self):
        return self.driver.find_element_by_class_name('controls_item_dashboard')

    def get_notifications_settings_button(self):
        return self.driver.find_element_by_class_name('controls_item_notifications')

    def get_apps_settings_button(self):
        return self.driver.find_element_by_class_name('controls_item_apps')

    def get_labs_settings_button(self):
        return self.driver.find_element_by_class_name('controls_item_labs')

    def get_notifications_switcher(self):
        return self.driver.find_element_by_id('user_permit_marketing_emails')

    def get_labs_switcher(self):
        return self.driver.find_element_by_id('labs_user_opt_in')

    def get_android_button(self):
        return self.driver.find_element_by_id('app_android')

    def get_ios_button(self):
        return self.driver.find_element_by_id('app_iphone')

    def get_delete_account_button(self):
        return self.driver.find_element_by_class_name('delete')

    def get_footer_link(self):
        return self.driver.find_element_by_class_name('footer_link')

    def get_messaging_button(self):
        return self.driver.find_element_by_id('messaging_button')

    def get_discover_button(self):
        return self.driver.find_element_by_id('discover_button')

    def get_create_button(self):
        return self.driver.find_element_by_class_name('compose-button')

    def get_inbox_button(self):
        return self.driver.find_element_by_id('inbox_button')

    def get_discover_types_buttons(self):
        return self.driver.find_element_by_class_name('types-tabs').find_elements_by_class_name('content-control')

    def get_discover_search_buttons(self):
        return self.driver.find_element_by_class_name('discover-search-terms').find_elements_by_class_name('discover-search-term')

    def get_post_type_selection_button(self, post_type):
        for button in self.driver.find_elements_by_class_name('tab-post-type'):
            if (button.get_attribute('data-post-type') == post_type):
                return button

    def get_create_post_button(self):
        return self.driver.find_element_by_class_name('create_post_button')

    def get_posts_button(self):
        for item in self.driver.find_elements_by_class_name('blog-sub-nav-item-link'):
                if 'Posts' in item.text:
                    return item

    def get_signup_login_button(self):
        return self.driver.find_element_by_id("signup_login_button")

    def get_logout_button(self):
        return self.driver.find_element_by_id('logout_button')

    def get_ok_button(self):
        return self.driver.find_element_by_class_name('btn_1')

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

