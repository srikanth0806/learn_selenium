from selenium import webdriver
from selenium.webdriver.common.by import By


class ElementState:

    def isenabled(self):
        baseurl = "https://cleardesign.co.uk/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        path = "//span[starts-with(@class, 'gi svg-social linkedin')]"
        x = driver.find_element(By.XPATH, path)
        elementstate = x.is_enabled()
        print(elementstate)


e = ElementState()
e.isenabled()
