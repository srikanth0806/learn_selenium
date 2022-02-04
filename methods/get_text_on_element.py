"""
    get text on web element.
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

        element = driver.find_element(By.XPATH, "//a[@id = 'opentab']")
        x = element.text
        print("the text ont the element is:" + x)
        time.sleep(2)
        driver.quit()


Gm = Getmethods()
Gm.test()
