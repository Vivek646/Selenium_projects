class PRACTICE:
    test_login = "//a[text()='Test Login Page']"
    test_exceptions = "//a[text()='Test Exceptions']"

    def __init__(self,driver):
        self.driver = driver

    def test_login_link(self):
        self.driver.find_element('xpath',self.test_login).click()

    def test_exceptions_link(self):
        self.driver.find_element('xpath',self.test_exceptions).click()
    