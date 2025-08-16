from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

driver.get("https://demo.itlearn360.com")

alllinks=driver.find_elements(By.TAG_NAME,'a')
print(len(alllinks))


for link in alllinks:
    url=link.get_attribute("href")
    print(url)