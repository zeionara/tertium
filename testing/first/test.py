import time
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.tumblr.com/');
elem = driver.find_element_by_class_name("signup_get_started_btn")
elem.click()

#time.sleep(5) # Let the user actually see something!
#search_box = driver.find_element_by_name('q')
#search_box.send_keys('pornhub')
#search_box.submit()

#header = driver.find_element_by_tag_name('h3')
#header.click()

#for handle in driver.window_handles:
#    driver.switch_to_window(handle)
#    print(driver.current_url)



#time.sleep(5) # Let the user actually see something!
#driver.quit()