from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.tynesidebadmintoncentre.co.uk/racket-maintenance/")

#Surname:
search = driver.find_element_by_id("form-field-name")
search.send_keys("KING LAST")

#First Name:
search = driver.find_element_by_id("form-field-field_3d9331e")
search.send_keys("KING FIRST")

time.sleep(30)
driver.quit()

#Telephone:
search = driver.find_element_by_id("form-field-field_4f81bfe")
search.send_keys("ZZZZZZZZZZZZZZZZZ")

#Email:



print(driver.title)