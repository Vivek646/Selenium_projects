import pytest

def test_five():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://www.flipkart.com/')
    time.sleep(2)
    driver.close()


def test_six():
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://open.spotify.com/')
    time.sleep(2)
    driver.close()
