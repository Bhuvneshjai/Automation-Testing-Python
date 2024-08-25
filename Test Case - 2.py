import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify the path of Edge Driver
service = Service(r"C:\Users\HP\Desktop\Projects\Projects_Code\Automation-Practice\Drivers\edgedriver_win64\msedgedriver.exe")

# Initialize the Edge Driver
edgeDriver = webdriver.Edge(service=service)

# Open the Website
edgeDriver.get("https://admin-demo.nopcommerce.com/login")

# Wait for username field to be present
WebDriverWait(edgeDriver, 10).until(EC.presence_of_element_located((By.NAME, "Email")))

# Provide Email
edgeDriver.find_element(By.NAME, "Email").send_keys("")

# Provide Password
edgeDriver.find_element(By.ID, "Password").send_keys("")

# Click Login Button
edgeDriver.find_element(By.CLASS_NAME, "login-button").click()

# Print the current title after login
print("Title after login:", edgeDriver.title)

# Get Title
actualTitle = "Dashboard / nopCommerce administration"
driverTitle = edgeDriver.title

# Verify Title
if actualTitle == driverTitle:
    print("Login Passed")
else:
    print("Login Failed")

# Keep the browser open for 50 seconds
time.sleep(50)

# Close the browser
edgeDriver.quit()
