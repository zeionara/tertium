import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from subprocess import call

CHROME_DRIVER_LOCATION = './chromedriver'
URL = "https://www.tumblr.com"

EMAIL = os.environ['EMAIL']
PASSWORD = os.environ['PASSWORD']

TEST_SCRIPTS_BEFORE_LOGIN = ['main.py']
TEST_SCRIPTS_AFTER_LOGIN = ['creation.py', 'discover.py']

def run_tests(scripts_list, driver):
	for script in scripts_list:
		print('Running tests from ' + script + ' ...')
		print(call(['python', script, '-v'], \
			env = {'SESSION_URL' : driver.command_executor._url, 'SESSION_ID' : driver.session_id, 
					'DISPLAY' : ':0.0', 'EMAIL' : EMAIL, 'PASSWORD' : PASSWORD}))

def show_session_info(driver):
	print('Session started')
	print('url : ' + driver.command_executor._url)
	print('session id : ' + driver.session_id)

def main():
    driver = webdriver.Chrome(CHROME_DRIVER_LOCATION)

    show_session_info(driver)
    run_tests(TEST_SCRIPTS_BEFORE_LOGIN, driver)

    driver.get(URL + "/login")
        
    email_field = driver.find_element_by_id("signup_determine_email")
    email_field.send_keys(EMAIL)
    email_field.send_keys(Keys.RETURN)

    time.sleep(2)

    password_field = driver.find_element_by_id("signup_password")
    password_field.send_keys(PASSWORD)
    password_field.send_keys(Keys.RETURN)

    run_tests(TEST_SCRIPTS_AFTER_LOGIN, driver)

    time.sleep(100500)

if __name__ == '__main__':
	main()