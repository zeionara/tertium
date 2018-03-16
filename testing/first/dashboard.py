import unittest
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

CHROME_DRIVER_LOCATION = './chromedriver'
URL = "https://www.tumblr.com/"

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']

INITIAL_NUMBER_OF_POSTS_TO_SHOW = 38

FOLLOWING_INDEX = 3

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

    def get_follow_buttons(self):
        return self.driver.find_elements_by_class_name("plus-follow-button");

    def get_dismiss_buttons(self):
        return self.driver.find_elements_by_class_name("dismiss");

    def get_dismiss_titles(self):
        return self.driver.find_elements_by_class_name("tumblelog_title");

    def get_account_button(self):
        return self.driver.find_element_by_id("account_button");

    def get_following(self):
        following = []
        for item in self.driver.find_elements_by_class_name("name-link"):
            following.append(item.text)
        return following

    def get_unfollow_button(self, follower):
        return self.driver.find_element_by_id("unfollow_button_"+follower)

    def get_follower_links(self):
        return self.driver.find_elements_by_class_name("follow_list_item_blog")

    def is_there_item_with_class(self, searched_class):
        try:
            self.driver.find_element_by_class_name(searched_class)
        except:
            return False
        return True

    def is_there_follower_container(self):
        return self.is_there_item_with_class("peepr-drawer-container")

    def is_there_glass_container(self):
        return self.is_there_item_with_class("ui_peepr_glass")

    def get_posts(self):
        return self.driver.find_elements_by_class_name("post")

    def get_like_button(self, post):
        return post.find_element_by_class_name("like")

    def get_like_button_by_post_id(self, post_id):
        for post in self.get_posts():
            if self.get_post_id(post) == post_id:
                return self.get_like_button(post)

    def get_post_id(self, post):
        return post.get_attribute('data-post-id')

    def is_there_post(self, post_id):
        print(post_id)
        for post in self.get_posts():
            print('oo')
            print(self.get_post_id(post))
            if self.get_post_id(post) == post_id:
                return True
        return False

    def get_liked_count(self):
        self.driver.find_element_by_id('account_button').click()
        time.sleep(1)
        try:
            for item in self.driver.find_elements_by_class_name('popover_menu_item_anchor'):
                print('href')
                print(item.get_attribute('href'))
                if item.get_attribute('href') == URL + 'likes':
                    return item.find_element_by_class_name("popover_item_suffix").text
        finally:
            self.driver.find_element_by_id('account_button').click()
        


@unittest.skip("skipping")
class FollowSuccess(DashboardTest):

    def test_follow_succeeded(self):
        driver = self.driver

        self.login()

        follow_buttons = self.get_follow_buttons()

        followed_title = follow_buttons[FOLLOWING_INDEX].get_attribute('data-tumblelog-name')
        follow_buttons[FOLLOWING_INDEX].click()

        self.driver.get(URL + "/following")

        assert followed_title in self.get_following()

        self.get_unfollow_button(followed_title).click()

        time.sleep(1)

        driver.find_element_by_class_name("btn_1").click()

        self.driver.refresh()

        assert followed_title not in self.get_following()


@unittest.skip("skipping")
class DismissSuccess(DashboardTest):

    def test_dismiss_succeeded(self):
        driver = self.driver

        self.login()

        dismiss_buttons = self.get_dismiss_buttons()
        dismiss_titles = self.get_dismiss_titles()

        dismiss_buttons[FOLLOWING_INDEX].click()

        time.sleep(1)

        assert dismiss_titles[FOLLOWING_INDEX].text not in self.get_dismiss_titles()

@unittest.skip("skipping")
class ShowCommunityInfoSuccess(DashboardTest):

    def test_show_community_info(self):
        driver = self.driver

        self.login()

        self.assertFalse(self.is_there_follower_container())
        self.assertFalse(self.is_there_glass_container())

        followers_links = self.get_follower_links()
        followers_links[FOLLOWING_INDEX].click()

        self.assertTrue(self.is_there_follower_container())
        self.assertTrue(self.is_there_glass_container())

#@unittest.skip("skipping")
class LikeSuccess(DashboardTest):

    def test_like_succeeded(self):
        driver = self.driver

        self.login()

        time.sleep(2)

        posts = self.get_posts()

        for post in posts:
            print(self.get_post_id(post))

        old_liked_count = int(str(self.get_liked_count()))

        print('old faa', old_liked_count)

        like_button = self.get_like_button(posts[4])

        post_id = self.get_post_id(posts[4])

        
        print('like)')

        print(like_button)

        like_button.click()

        self.driver.get(URL + "/likes")

        self.assertTrue(self.is_there_post(post_id))

        print('aaaaaaaa')

        newa = int(str(self.get_liked_count()))

        print('current ', newa)
        print('old ',old_liked_count)
        
        self.assertEquals(newa, old_liked_count + 1)

        time.sleep(2)

        self.get_like_button_by_post_id(post_id).click()

        driver.refresh()

        newa = int(str(self.get_liked_count()))

        self.assertEquals(newa, old_liked_count)


if __name__ == "__main__":
    unittest.main()