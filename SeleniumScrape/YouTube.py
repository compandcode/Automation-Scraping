from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https:www.youtube.com")

searchBar = driver.find_element_by_tag_name("input")
searchBar.send_keys("Clever Programmer")
#searchBar.send_keys(Keys.RETURN)