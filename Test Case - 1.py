import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path of chrome driver
service = Service(r"C:\Users\HP\Desktop\Projects\Projects_Code\Automation-Practice\Drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")

# Initialize the Chrome Driver
chromeDriver = webdriver.Chrome(service=service)

# Open the Website
chromeDriver.get("https://opensource-demo.orangehrmlive.com")

# Wait for Username field to be present
WebDriverWait(chromeDriver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

# Provide Username
chromeDriver.find_element(By.NAME, "username").send_keys("Admin")

# Provide Password
chromeDriver.find_element(By.NAME, "password").send_keys("admin123")

# Click Login Button
chromeDriver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()

# Wait for the title to be present
WebDriverWait(chromeDriver, 10).until(EC.title_contains("OrangeHRM"))

# Get Title
actualTitle = "OrangeHRM"
driverTitle = chromeDriver.title

# Verify Title
if actualTitle == driverTitle:
    print("Login Test Passed")
else:
    print("Login Test Failed")

# Keep the browser open for 50 seconds
time.sleep(50)

# Close the browser
chromeDriver.quit()
