from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

PATH = "PUT THE PATH HERE!!"
driver = webdriver.Chrome(PATH)

currentUrl = driver.get("https://en-gb.facebook.com/")
print(driver.title)

#Email/Phone Number
phoneNumber = driver.find_element_by_id("email")
phoneNumber.send_keys("") #Enter email or phone number here.

password = driver.find_element_by_id("pass")
password.send_keys("") #Enter oassword here.
password.send_keys(Keys.RETURN)

#search = driver.find_element_by_class_name("a-row")
#print(search)

currentUrl = driver.current_url #Once Logged in, changes the URL
