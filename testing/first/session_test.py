import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

URL = "https://www.tumblr.com"

SESSION_URL = os.environ['SESSION_URL']
SESSION_ID = os.environ['SESSION_ID']

def main():
    driver = webdriver.Remote(command_executor = SESSION_URL, desired_capabilities={})
    driver.session_id = SESSION_ID

    driver.get(URL + "/me")

if __name__ == '__main__':
	main()