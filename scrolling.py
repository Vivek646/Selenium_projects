import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)

ob = ActionChains(driver)

# to scroll based on axis value
# ob.scroll_by_amount(0,1000).perform()
# time.sleep(2)
# ob.scroll_by_amount(0,-1000).perform()


# it will scroll upto specified element
# ele = driver.find_element(By.XPATH, '//*[@id="animals"]')
# ob.scroll_to_element(ele).perform()


# to scroll from top to bottom
# driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
# time.sleep(2)


# to scroll from bottom to top
# driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")


# to get max y-axis value (total scrollable height of the page)
# first scroll a little bit 
# driver.execute_script("window.scrollTo(0,1500)") 
# current_y = driver.execute_script("return window.pageYOffset")
# max_y = driver.execute_script("return document.body.scrollHeight")
# print(max_y)


# to scroll based on axis
driver.execute_script("window.scrollBy(0, 2000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0, -1000)")
time.sleep(2)
driver.execute_script("window.scrollBy(0, -1000)")


# horizontal scroll
# to scroll from left to right
# ele = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div[2]")
# driver.execute_script("window.scrollBy(document.body.scrollWidth, 0)")





time.sleep(3)