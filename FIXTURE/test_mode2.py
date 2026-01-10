import pytest

def test_three(setup):
    driver = setup
    driver.get('https://www.shoppersstack.com/')


def test_four(setup):
    driver = setup
    driver.get('https://www.amazon.in/')