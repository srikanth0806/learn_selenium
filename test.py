import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://courses.letskodeit.com/practice")
#driver.implicitly_wait(20)
# elem = driver.find_element(By.XPATH, "//td[@class='course-name']")
# print(elem)
print("--------------------------")
elem = driver.find_elements(By.XPATH, "//td[@class='course-name']")
elements  = driver.find_elements_by_xpath("//td[@class='course-name']")
print(elem)
print("=================")
print(elements)
driver.close()






# driver.find_element(By.ID, "value")
# driver.find_element_by_id("value")
#
# driver.find_element(By.NAME, "value")
# driver.find_element_by_name("value")
#
# driver.find_element(By.XPATH, "some_xpath")
# driver.find_element_by_xpath("some_xpath")