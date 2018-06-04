import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = 'Zyra'
desired_caps['app'] = 'C:/Users/prote/Documents/appium/com.facebook.lite_96.0.0.7.216-110083574_minAPI9(x86)(nodpi)_apkmirror.com.apk'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

current = driver.current_context

print(current)

el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup")
el1.click()
el1.send_keys("hello")
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[1]/android.view.ViewGroup[4]/android.view.ViewGroup")
el2.click()
el2.send_keys("hello")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup")
el3.click()
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.ViewGroup")
el4.click()

TouchAction(driver).tap(x=130, y=215).perform()
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[1]/android.view.ViewGroup[2]")
el1.send_keys("hello")
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[1]/android.view.ViewGroup[4]")
el2.send_keys("world")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup")
el3.click()
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup")
el4.click()
el5 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup")
el5.send_keys("hello@gmail.com")
el6 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[1]/android.view.ViewGroup[4]")
el6.send_keys("world")
el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/X.03C/android.view.ViewGroup[2]/android.view.ViewGroup/android.view.ViewGroup")
el7.click()