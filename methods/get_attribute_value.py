"""
    get value attribute in web elment.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Getmethods:

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        baseurl = "https://courses.letskodeit.com/practice"
        driver.get(baseurl)
        driver.implicitly_wait(20)

        element = driver.find_element(By.XPATH,
                                      "//input[@placeholder = 'Enter Your Name']")
        x = element.get_attribute("class")
        print("the value of class attribute  is:" + x)
        time.sleep(2)
        driver.quit()
        element.find_element_by_id()


Gm = Getmethods()
Gm.test()
