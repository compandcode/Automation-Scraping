from selenium import webdriver
import time

#"C:\Program Files (x86)\chromedriver.exe"
PATH = "C:\Users\Vikra\Desktop\New folder\Automation-Scraping\BlogPostViews\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.thenibblebyte.com/blog/categories/compandcode")
time.sleep(10)
driver.close()
