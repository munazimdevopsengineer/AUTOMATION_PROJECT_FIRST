'''from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://selenium.dev/')
input("Press Enter to close the browser...")
driver.quit()'''



from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://selenium.dev/')
time.sleep(5)  # Keep the browser open for 5 seconds
driver.quit()



