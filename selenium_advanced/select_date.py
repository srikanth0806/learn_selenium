"""
    automate the date in calender.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class CalenderSelection:

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        url = "https://www.expedia.co.in/"
        driver.get(url)
        driver.implicitly_wait(10)

        check_in_element = driver.find_element(By.ID,"d1-btn").click()
        #check_in_element.click()

        element = driver.find_element(By.XPATH, "//button[@data-day='17']")
        element.click()
        time.sleep(10)
        done = driver.find_element(By.XPATH, "//button[@data-stid='apply-date-picker']")
        done.click()
        print("done  clicked")


cc = CalenderSelection()
cc.test()
print("execution completed")