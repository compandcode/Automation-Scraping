from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.thenibblebyte.com/blog/categories/compandcode")
time.sleep(10)

blogPosts = driver.find_element_by_class_name("MlM6L").text

for post in blogPosts:
    print(blogPosts)