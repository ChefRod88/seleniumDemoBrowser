import time
from selenium import webdriver
driver = webdriver.Chrome() #invokes Chrome browser
driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)


















































time.sleep(2)