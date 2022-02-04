import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
driver.maximize_window()
time.sleep(15)
print(driver.current_url)
driver.close()