import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = r"C:\Users\sRIKANTH\Downloads\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://courses.letskodeit.com/practice")
driver.maximize_window()
radio_button1 = driver.find_element(By.ID, "bmwradio")
radio_button1.click()
time.sleep(3)
radio_button2 = driver.find_element(By.ID, "benzradio")
radio_button2.click()
time.sleep(3)
radio_button3 = driver.find_element(By.ID, "hondaradio")
radio_button3.click()


webelement_name = driver.find_element(By.XPATH, " //input[@name='enter-name']")
webelement_name.send_keys("Tallapalli Srikanth")


# bmw = driver.find_element(By.XPATH, "//option[@value='honda']")
# bmw.click()

#driver.close()