# send data -> copy & paste into other textfield -> remove the passed data
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)

ob = ActionChains(driver)

text_box = driver.find_element(By.ID, 'name')
text_box.send_keys('vivek')
time.sleep(1)
ob.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
time.sleep(1)
ob.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
time.sleep(1)
ob.key_down(Keys.TAB).perform()
time.sleep(1)
ob.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
time.sleep(1)
ob.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
time.sleep(1)
ob.key_down(Keys.BACKSPACE).perform()


time.sleep(2)