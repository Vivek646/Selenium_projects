import pytest

def test_five():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://testautomationpractice.blogspot.com/')
    time.sleep(2)
    driver.close()

def test_six():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.facebook.com/')
    time.sleep(2)
    driver.close()