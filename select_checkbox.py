import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = r"C:\Users\sRIKANTH\Downloads\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://courses.letskodeit.com/practice")
driver.maximize_window()
check_box1 = driver.find_element(By.ID, "bmwcheck")
check_box1.click()
check_box2 = driver.find_element(By.ID, "benzcheck")
check_box2.click()
check_box3 = driver.find_element(By.ID, "hondacheck")
check_box3.click()

# bmw = driver.find_element(By.XPATH, "//option[@value='honda']")
# bmw.click()

#driver.close()