from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

driver.get("https://training.qaonlinetraining.com/testPage.php")

driver.find_element(By.NAME,'name').send_keys("Munna")
driver.find_element(By.NAME,'email').send_keys("ravi@gmail.com")
driver.find_element(By.NAME,'website').send_keys("https://ravi.com")
driver.find_element(By.NAME,'comment').send_keys("do not click")
driver.find_element(By.NAME,'submit').click()