from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InteractionBrowser:
    def test(self):
        baseurl = "https://www.facebook.com/"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseurl)
        driver.implicitly_wait(10)

        emailfield = driver.find_element(By.ID, "email")
        emailfield.send_keys(8919521056)

        passwordfield = driver.find_element(By.ID, "pass")
        passwordfield.send_keys("talla123@")
        time.sleep(5)

        loginlink = driver.find_element(By.NAME, "login")
        loginlink.click()
        time.sleep(30)


ib = InteractionBrowser()
ib.test()
