import pytest

def test_one():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://practicetestautomation.com/practice-test-login/')
    time.sleep(2)
    driver.close()


def test_two():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://demoapps.qspiders.com/ui?scenario=1')
    time.sleep(2)
    driver.close()