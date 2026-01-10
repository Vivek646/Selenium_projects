class LOGIN:
    un = 'username'
    pwd = 'password'
    submit = 'submit'

    def __init__(self,driver):
        self.driver = driver

    def un_text(self,username):
        self.driver.find_element('id',self.un).send_keys(username)

    def pwd_text(self,password):
        self.driver.find_element('id',self.pwd).send_keys(password)

    def submit_button(self):
        self.driver.find_element('id',self.submit).click()
        