from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

driver.get("https://training.qaonlinetraining.com/testPage.php")

driver.find_element(By.ID,'alert').click()

alert1=driver.switch_to.alert
print(f"The text from alert box {alert1.text}")

alert1.accept()

driver.find_element(By.ID,'confirm').click()

alert2=driver.switch_to.alert

alert2.dismiss()


driver.find_element(By.ID,'prompt').click()
alert3=driver.switch_to.alert

alert3.send_keys("Itlearn")
alert3.accept()

