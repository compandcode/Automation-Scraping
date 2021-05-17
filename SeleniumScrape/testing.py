from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com")
print(driver.title)

search = driver.find_element_by_name("q")
search.send_keys("cleverprogrammer")
search.send_keys(Keys.RETURN)

main = driver.find_element_by_id()
print(main.text)

driver.quit()

