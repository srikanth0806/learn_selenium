"""
    write a programme to select one opotion.
"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class SelectOption:
    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        baseurl = "https://www.southwest.com/"
        driver.get(baseurl)
        driver.implicitly_wait(5)
        time.sleep(5)

        class_element = driver.find_element(By.XPATH, '//span[text()="Hotel"]' )
        class_element.click()

        time.sleep(5)

        input_element = driver.find_element(By.XPATH, '//input[@id="b_destination and @name="ss""]')
        input_element.click()
        input_element.send_keys("mal")
        driver.implicitly_wait(5)
        time.sleep(5)
        option_element = driver.find_element(By.XPATH, '//ul[@id="ui-id-1" ]//li[contains(text(),"Mallorca, Spain")]')
        option_element.click()
        time.sleep(5)

        #driver.quit()


so = SelectOption()
so.test()
