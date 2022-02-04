import time
from selenium import webdriver

firefox_driver_path = r"C:\Users\sRIKANTH\Downloads\drivers\geckodriver.exe"
driver = webdriver.Firefox(executable_path=firefox_driver_path)

driver.get("https://www.facebook.com")
driver.maximize_window()
time.sleep(3)
print(driver.current_url)
driver.close()
