import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)

# taking screenshot of the whole page
driver.save_screenshot('demo1.png')

# taking screenshot of a single element
ele = driver.find_element(By.CLASS_NAME, 'start')
ele.screenshot('start_btn_ss.png')


time.sleep(2)