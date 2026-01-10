import pytest

def test_five(setup):
    driver = setup
    driver.get('https://www.zomato.com/kolkata')


def test_six(setup):
    driver = setup
    driver.get('https://open.spotify.com/')