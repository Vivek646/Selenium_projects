import pytest

def test_one(setup):
    driver = setup
    driver.get('https://testautomationpractice.blogspot.com/')


def test_two(setup):
    driver = setup
    driver.get('https://demoapps.qspiders.com/ui?scenario=1')