import time
from selenium import webdriver

#chrome_driver_path = r"C:\Users\sRIKANTH\Downloads\drivers\chromedriver.exe"
#driver = webdriver.Chrome(executable_path=chrome_driver_path)

# crome driver is installed in the current directory or python path.

driver = webdriver.Chrome()

driver.get("https://www.facebook.com")
driver.maximize_window()
time.sleep(3)
print(driver.current_url)


driver.close()