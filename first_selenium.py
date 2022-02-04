import time

from selenium import webdriver
from selenium.webdriver.common.by import By

gecko_dirver_path = r"C:\Users\sRIKANTH\Downloads\drivers\geckodriver.exe"
edge_driver_path = r"C:\Users\sRIKANTH\Downloads\drivers\msedgedriver.exe"
chrome_driver_path = r"C:\Users\sRIKANTH\Downloads\drivers\chromedriver.exe"
#driver = webdriver.Chrome(chrome_driver_path)
driver = webdriver.Firefox(executable_path=gecko_dirver_path)
#driver = webdriver.Edge(edge_driver_path)

driver.get("https://www.facebook.com")
# driver.maximize_window()
# time.sleep(3)
# mail = driver.find_element(By.ID, "email")
# mail.send_keys("srikanth@gmail.com")
# time.sleep(2)

driver.close()