import time
import Utilities
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r"https://www.sbisecurities.in/calculators/loan-emi-calculator")
driver.maximize_window()
time.sleep(2)
path = "E:\worksheet.xlsx"

rows = Utilities.row_count(path,"Sheet2")
for r in range(2,rows+1):
    amount = Utilities.read_data(path,"Sheet2",r,1)
    tenure = Utilities.read_data(path,"Sheet2",r,2)
    interest = Utilities.read_data(path, "Sheet2", r, 3)
    exp_amt = Utilities.read_data(path, "Sheet2", r, 4)
    act_amt = Utilities.read_data(path, "Sheet2", r, 5)
    status = Utilities.read_data(path, "Sheet2", r, 6)

    driver.find_element("xpath","//input[@placeholder='Enter Loan Amount']").clear()
    driver.find_element("xpath", "//input[@placeholder='Enter Loan Amount']").send_keys(amount)
    time.sleep(1)

    driver.find_element("xpath", "//input[@placeholder='Enter Time']").clear()
    driver.find_element("xpath", "//input[@placeholder='Enter Time']").send_keys(tenure)
    time.sleep(1)

    driver.find_element("id", "input_interest").clear()
    driver.find_element("id", "input_interest").send_keys(interest)
    time.sleep(1)

    driver.find_element("xpath", "//button[text()='Calculate']").click()
    time.sleep(1)

    act_amt = driver.find_element("xpath", "//span[@class='green--txt']").text
    act_amt = act_amt[1::]
    act_amt = act_amt.replace(",","",1)

    if act_amt == str(exp_amt):
        print("test is passed")
        Utilities.write_data(path,"Sheet2",r,5,act_amt)
        Utilities.write_data(path,"Sheet2",r,6,"pass")
    else:
        print("test is failed")
        Utilities.write_data(path, "Sheet2", r, 5, act_amt)
        Utilities.write_data(path, "Sheet2", r, 6, "fail")
    time.sleep(1)
time.sleep(3)