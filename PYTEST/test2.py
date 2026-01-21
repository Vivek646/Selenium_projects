import pytest

def test_three():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')
    time.sleep(2)
    driver.close()


def test_four():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://www.zomato.com/')
    time.sleep(2)
    driver.close()