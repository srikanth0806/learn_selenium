"""
   write a  programme on implicit wait.
"""

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def wait_implicitly():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = "https://letskodeit.teachable.com/p/practice"
    driver.get(url)
    driver.implicitly_wait(10)

    login_element = driver.find_element(By.XPATH, "//a[@href='/sign_in']")
    login_element.click()

    email_element = driver.find_element(By.XPATH, "//input[@id='email']")
    email_element.send_keys("srikanth@gmail.com")
    time.sleep(10)

    driver.quit()


wait_implicitly()
