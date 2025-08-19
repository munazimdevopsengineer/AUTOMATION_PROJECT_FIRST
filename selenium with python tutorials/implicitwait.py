from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

driver.get("https://demo.itlearn360.com/")
driver.implicitly_wait(10)

driver.find_element(By.ID,'loginlabel').click()

driver.find_element(By.NAME,'log').send_keys("Demo12")

driver.find_element(By.NAME,'pwd').send_keys("Test123456$")
driver.find_element(By.NAME,'wp-submit').click()

