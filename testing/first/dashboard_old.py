import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

from utils import PostOperator, PresenceChecker, ButtonGetter

CHROME_DRIVER_LOCATION = './chromedriver'
URL = "https://www.tumblr.com/"

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']
POST_NOTE = os.environ['POST_NOTE']

INITIAL_NUMBER_OF_POSTS_TO_SHOW = 38

FOLLOWING_INDEX = 3
FIRST_POST_INDEX = 2


class DashboardTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_LOCATION)
        self.driver.get(URL + "/login")

    def login(self):
        driver = self.driver
        
        email_field = self.driver.find_element_by_id("signup_determine_email")
        email_field.send_keys(EMAIL)
        email_field.send_keys(Keys.RETURN)

        time.sleep(2)

        password_field = self.driver.find_element_by_id("signup_password")
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.RETURN)

        assert "Sign up" not in driver.title

    def tearDown(self):
        self.driver.close()

    def get_dismiss_titles(self):
        return self.driver.find_elements_by_class_name("tumblelog_title");

    def get_following(self):
        following = []
        for item in self.driver.find_elements_by_class_name("name-link"):
            following.append(item.text)
        return following

    def get_follower_links(self):
        return self.driver.find_elements_by_class_name("follow_list_item_blog")

    def get_liked_count(self):
        self.driver.find_element_by_id('account_button').click()
        time.sleep(1)
        try:
            for item in self.driver.find_elements_by_class_name('popover_menu_item_anchor'):
                if item.get_attribute('href') == URL + 'likes':
                    return item.find_element_by_class_name("popover_item_suffix").text
        finally:
            self.driver.find_element_by_id('account_button').click()

    def get_posted_count(self):
        self.driver.find_element_by_id('account_button').click()
        time.sleep(1)
        try:
            for item in self.driver.find_elements_by_class_name('blog-sub-nav-item-link'):
                if item.find_element_by_class_name('blog-sub-nav-item-label').text == 'Posts':
                    return int(str(item.find_element_by_class_name("blog-sub-nav-item-data").text))
        finally:
            self.driver.find_element_by_id('account_button').click()

    def get_reblog_text_field(self):
        return self.driver.find_element_by_class_name('editor-richtext')

    def get_post_avatar_link(self):
        return self.driver.find_element_by_class_name('post_avatar_link')

#@unittest.skip("skipping")
class FollowSuccess(DashboardTest):

    def test_follow_succeeded(self):
        driver = self.driver
        self.login()

        button_getter = ButtonGetter(driver)

        follow_buttons = button_getter.get_follow_buttons()

        followed_title = follow_buttons[FOLLOWING_INDEX].get_attribute('data-tumblelog-name')
        follow_buttons[FOLLOWING_INDEX].click()

        self.driver.get(URL + "/following")

        assert followed_title in self.get_following()

        button_getter.get_unfollow_button(followed_title).click()

        time.sleep(1)

        driver.find_element_by_class_name("btn_1").click()

        self.driver.refresh()

        assert followed_title not in self.get_following()


#@unittest.skip("skipping")
class DismissSuccess(DashboardTest):

    def test_dismiss_succeeded(self):
        driver = self.driver
        self.login()

        button_getter = ButtonGetter(driver)

        dismiss_buttons = button_getter.get_dismiss_buttons()
        dismiss_titles = self.get_dismiss_titles()

        dismiss_buttons[FOLLOWING_INDEX].click()

        time.sleep(1)

        assert dismiss_titles[FOLLOWING_INDEX].text not in self.get_dismiss_titles()

#@unittest.skip("skipping")
class ShowCommunityInfoSuccess(DashboardTest):

    def test_show_community_info(self):
        driver = self.driver
        self.login()

        presence_checker = PresenceChecker(driver)

        self.assertFalse(presence_checker.is_there_follower_container())
        self.assertFalse(presence_checker.is_there_glass_container())

        followers_links = self.get_follower_links()
        followers_links[FOLLOWING_INDEX].click()

        self.assertTrue(presence_checker.is_there_follower_container())
        self.assertTrue(presence_checker.is_there_glass_container())

#@unittest.skip("skipping")
class LikeSuccess(DashboardTest):

    def test_like_succeeded(self):
        driver = self.driver
        self.login()

        post_operator = PostOperator(driver)
        button_getter = ButtonGetter(driver)
        presence_checker = PresenceChecker(driver)

        time.sleep(2)

        posts = post_operator.get_posts()

        old_liked_count = int(str(self.get_liked_count()))
        like_button = button_getter.get_like_button(posts[FIRST_POST_INDEX + FOLLOWING_INDEX])
        post_id = post_operator.get_post_id(posts[FIRST_POST_INDEX + FOLLOWING_INDEX])

        like_button.click()

        time.sleep(1)

        assert 'liked' in like_button.get_attribute('class')

        self.driver.get(URL + "/likes")

        self.assertTrue(presence_checker.is_there_post(post_operator, post_id))

        new_liked_count = int(str(self.get_liked_count()))
        
        self.assertEquals(new_liked_count, old_liked_count + 1)

        time.sleep(2)

        button_getter.get_like_button_by_post_id(post_operator, post_id).click()

        driver.refresh()

        assert button_getter.get_like_button_by_post_id(post_operator, post_id) is None

        new_liked_count = int(str(self.get_liked_count()))

        self.assertEquals(new_liked_count, old_liked_count)

#@unittest.skip("skipping")
class ShareSuccess(DashboardTest):

    def test_share_succeeded(self):
        driver = self.driver
        self.login()

        button_getter = ButtonGetter(driver)
        presence_checker = PresenceChecker(driver)
        post_operator = PostOperator(driver)

        post = post_operator.get_posts()[FIRST_POST_INDEX + FOLLOWING_INDEX]
        post_id = post_operator.get_post_id(post)
        button_getter.get_share_button(post).click()

        time.sleep(2)

        button_getter.get_permalink_button().click()
        self.assertTrue(presence_checker.is_there_tab_with_url_part(post_id))

        time.sleep(1)

        self.assertFalse(presence_checker.is_there_item_with_class('back-button'))
        self.assertFalse(presence_checker.is_there_item_with_class('embed-code'))
        button_getter.get_embed_button().click()

        time.sleep(1)

        self.assertTrue(presence_checker.is_there_item_with_class('back-button'))
        self.assertTrue(presence_checker.is_there_item_with_class('embed-code'))
        driver.find_element_by_class_name('back-button').click()

        time.sleep(1)

        self.assertFalse(presence_checker.is_there_item_with_class('back-button'))
        self.assertFalse(presence_checker.is_there_item_with_class('embed-code'))
        self.assertFalse(presence_checker.is_there_glass_container())
        self.assertFalse(presence_checker.is_there_drawer_container())

        button_getter.get_report_button().click()

        time.sleep(1)

        self.assertTrue(presence_checker.is_there_glass_container())
        self.assertTrue(presence_checker.is_there_drawer_container())

#@unittest.skip("skipping")
class ReblogSuccess(DashboardTest):

    def test_reblog_succeeded(self):
        driver = self.driver
        self.login()

        button_getter = ButtonGetter(driver)
        presence_checker = PresenceChecker(driver)
        post_operator = PostOperator(driver)

        post = post_operator.get_posts()[FIRST_POST_INDEX + FOLLOWING_INDEX]
        post_id = post_operator.get_post_id(post)

        old_posted_count = self.get_posted_count()

        #print('old posted count:', old_posted_count)

        button_getter.get_reblog_button(post).click()

        time.sleep(1)

        self.assertTrue(presence_checker.is_there_post_modal_container())

        self.get_reblog_text_field().send_keys(POST_NOTE)

        post_settings_button = button_getter.get_post_settings_button()

        self.assertFalse(presence_checker.is_there_post_settings_dropdown())
        post_settings_button.click()

        time.sleep(1)

        self.assertTrue(presence_checker.is_there_post_settings_dropdown())
        post_settings_button.click()

        time.sleep(1)

        button_getter.get_reblog_applying_button().click()

        time.sleep(2)

        new_posted_count = self.get_posted_count()

        #print('new posted count:', new_posted_count)

        self.assertEquals(old_posted_count + 1, new_posted_count)

        self.driver.get(self.get_post_avatar_link().get_attribute('href'))

        self.assertTrue(presence_checker.is_there_reblogged_post(post_operator, post_id, POST_NOTE))

if __name__ == "__main__":
    unittest.main()