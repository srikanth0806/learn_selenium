import time
from selenium import webdriver

edge_driver_path = r"C:\Users\sRIKANTH\Downloads\drivers\msedgedriver.exe"
driver = webdriver.Edge(executable_path=edge_driver_path)

driver.get("https://www.facebook.com")
driver.maximize_window()
time.sleep(3)
print(driver.current_url)
driver.close()