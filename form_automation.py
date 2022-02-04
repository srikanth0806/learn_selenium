import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("file:///C:/Users/sRIKANTH/Desktop/learn_selenium/html/appliction1.html")

driver.maximize_window()
driver.implicitly_wait(10)

time.sleep(5)
webelement_name=driver.find_element(By.ID,"")
webelement_name.send_keys("srikanth")

#driver.close()
