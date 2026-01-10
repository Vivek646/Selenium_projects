import pytest

def test_three():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://qspiders.com/')
    time.sleep(2)
    driver.close()

def test_four():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.amazon.in/')
    time.sleep(2)
    driver.close()