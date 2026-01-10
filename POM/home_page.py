class HOME:
    practice = "//a[text()='Practice']"
    logout = "//a[text()='Log out']"

    def __init__(self, driver):
        self.driver = driver

    def practice_link(self):
        self.driver.find_element('xpath', self.practice).click()

    def logout_link(self):
        self.driver.find_element('xpath', self.logout).click()
