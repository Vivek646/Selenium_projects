import time
from DDT import Utilities
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
time.sleep(2)

path = "E:\worksheet.xlsx"
rows = Utilities.row_count(path, 'Sheet1')

for r in range(1,rows+1):
    UN = Utilities.read_data(path, 'Sheet1', r, 1)
    PWD = Utilities.read_data(path, 'Sheet1', r, 2)
    driver.find_element('name', 'username').clear()
    driver.find_element('name', 'username').send_keys(UN)
    time.sleep(1)
    driver.find_element('name', 'password').clear()
    driver.find_element('name', 'password').send_keys(PWD)
    time.sleep(1)
    driver.find_element('xpath', '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    time.sleep(3)

    if driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index':
        print('test is passed')
        Utilities.write_data(path, 'Sheet1', r, 4, 'pass')
        driver.find_element('xpath', '//span[@class="oxd-userdropdown-tab"]').click()
        driver.find_element('xpath', "//a[text()='Logout']").click()
        time.sleep(2)
    else:
        print('test is failed')
        Utilities.write_data(path, 'Sheet1', r, 4, 'fail')
    time.sleep(1)
time.sleep(3)
