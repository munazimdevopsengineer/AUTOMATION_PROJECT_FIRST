from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

driver.get("https://demo.itlearn360.com")
