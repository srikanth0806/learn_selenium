import time
from selenium import webdriver
from selenium.webdriver.common.by import By
#chrome_driver_path = r"C:\Users\sRIKANTH\Downloads\drivers\chromedriver.exe"
driver = webdriver.Chrome()    #the above path is already exist in lib

driver.get("https://courses.letskodeit.com/practice")
driver.maximize_window()
drop_down = driver.find_element(By.ID, "carselect")
drop_down2 = driver.find_element_by_id("carselect")
#test = driver.find_elements_by_tag_name()
print((drop_down, drop_down2))

drop_down.click()

bmw = driver.find_element(By.XPATH, "//option[@value='honda']")
bmw.click()

#driver.close()