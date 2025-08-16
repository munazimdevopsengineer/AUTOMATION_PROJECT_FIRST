from selenium import webdriver
import time

viewports = [(1024,768),(786,1024),(375,667),(414,896)]

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

driver.set_window_size(width=768,height=1024)
time.sleep(6)
try:
    for width,height in viewports:
        driver.set_window_size(width,height)
        time.sleep(4)

finally:
    driver.close()

