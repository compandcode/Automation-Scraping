from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

for i in range(40):
    currentUrl = driver.get("https://www.thenibblebyte.com/post/why-online-courses-are-not-the-best-way-to-learn-computer-science-and-what-alternatives-are-there")
    print(driver.title)
    time.sleep(3)
    driver.quit()
    time.sleep(300)



