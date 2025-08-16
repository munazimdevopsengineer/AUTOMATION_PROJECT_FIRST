import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

browser= webdriver.Firefox()
browser.get('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')
browser.maximize_window()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
browser.find_element(By.XPATH,value="//input[@id='hobbies']").click()
time.sleep(5)
browser.find_element(By.XPATH,value="//div[7]//div[1]//div[1]//div[2]//input[1]").click()
time.sleep(5)
