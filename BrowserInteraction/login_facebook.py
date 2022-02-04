import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#chrome_driver_path = r"C:\Users\sRIKANTH\Downloads\drivers\chromedriver.exe"
driver = webdriver.Edge()

driver.get("https:www.facebook.com")
driver.maximize_window()
webelement_name = driver.find_element(By.XPATH, " //*[@id='email']")
webelement_name.send_keys("9603854911")
webelement_password = driver.find_element(By.XPATH, " //*[@id='pass']")
webelement_password.send_keys("9603854911")
time.sleep(3)
button = driver.find_element(By.XPATH, " //*[@id='u_0_d_ed']")
button.click()




# bmw = driver.find_element(By.XPATH, "//option[@value='honda']")
# bmw.click()

#driver.close()