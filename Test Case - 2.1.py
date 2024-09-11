import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Initialize Chrome Driver
service = Service()
chrome_Driver = webdriver.Chrome(service=service)

try:
    # Open the website
    chrome_Driver.get("https://www.facebook.com/")

    # Maximize the browser window
    chrome_Driver.maximize_window()
    time.sleep(2)

    # Custom CSS Selector
    # Tag and ID
    chrome_Driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("bhuvneshjain")
    time.sleep(2)

    # Tag and Class
    chrome_Driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("1234")
    time.sleep(2)

    # Tag and Attribute
    chrome_Driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("samyjain")
    time.sleep(2)

    # Tag, Class and Attribute
    chrome_Driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_pass]").send_keys("8979243823")
    time.sleep(2)

    print("Run Completed")

except Exception as e:
    print(f"An error occured: {e}")

# Optional sleep to view the final page before closing
time.sleep(30)

# Close the browser after tasks are completed
chrome_Driver.quit()
