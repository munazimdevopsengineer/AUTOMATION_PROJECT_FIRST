from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

driver.get("https://the-internet.herokuapp.com/nested_frames")

driver.switch_to.frame("frame-top")

#switch to next frame
driver.switch_to.frame("frame-middle")

content=driver.find_element(By.ID,'content').text
print("content in middle frame",content)
driver.switch_to.default_content()
driver.switch_to.frame("frame-bottom")
content_bottom=driver.find_element(By.TAG_NAME,'body').text
print("content in bottom",content_bottom)




#http://swisnl.github.io/jQuery-contextMenu/demo.html