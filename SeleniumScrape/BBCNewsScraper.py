from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
website = driver.get("https://bbc.co.uk/news" )

#Title = driver.find_elements_by_tag_name("h3")
#print(Title)

headlines = []

f = open("text.txt","w")

for element in driver.find_elements_by_tag_name("h3"):
    if element != "": #Gets rid of null values.
        headlines.append(element.text)
        f.write(element.text+ "\n")

#print(headlines)


f.close()
time.sleep(5)
driver.quit()

