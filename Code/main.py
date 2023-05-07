from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time


PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com")
print(driver.title)


time.sleep(10)
driver.quit()