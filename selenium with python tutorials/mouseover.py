from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.ebay.com/")

mouseoverelement=driver.find_element(By.XPATH,'//*[@id="gh"]/nav/div[2]/div[2]/a/span')

action=ActionChains(driver)

action.move_to_element(mouseoverelement).perform()

