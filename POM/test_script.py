from login_page import LOGIN
from home_page import HOME
from practice_page import PRACTICE

def test_case(setup):
    driver = setup
    driver.get('https://practicetestautomation.com/practice-test-login/')
    L = LOGIN(driver)
    L.un_text('student')
    L.pwd_text('Password123')
    L.submit_button()
    H = HOME(driver)
    H.practice_link()
    P = PRACTICE(driver)
    P.test_exceptions_link()