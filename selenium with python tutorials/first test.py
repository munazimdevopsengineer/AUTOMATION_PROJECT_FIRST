from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("http://selenium.dev/")
driver.maximize_window()
title = driver.title
print(title)
assert "Selenium123" in title

driver.find_element(By.XPATH("#APjFqb"))