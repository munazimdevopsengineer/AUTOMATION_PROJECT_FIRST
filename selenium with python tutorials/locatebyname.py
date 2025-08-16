from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
driver.find_element(By.NAME,value="q").send_keys("Selenium")
