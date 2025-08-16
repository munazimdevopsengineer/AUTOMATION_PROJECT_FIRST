from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)

# Type search query
driver.find_element(By.NAME, value="q").send_keys("Naveen Automation labs")

# Wait until at least some suggestions load
WebDriverWait(driver, timeout=4).until(
    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul[role='listbox'] li .innVSe"))
)

# Retry loop to catch suggestion even if it appears late
clicked = False
for _ in range(5):  # Retry up to 5 times
    optionlist: list[WebElement] = driver.find_elements(By.CSS_SELECTOR, "ul[role='listbox'] li .innVSe")
    print(f"Found {len(optionlist)} suggestions:")

    for ele in optionlist:
        text = ele.text.strip().lower()
        print(text)
        if text == "naveen automation labs youtube":
            ele.click()
            clicked = True
            break

    if clicked:
        break
    time.sleep(0.5)  # Small pause before checking again

time.sleep(5)
driver.quit()
