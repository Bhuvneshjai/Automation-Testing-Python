import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Initialize the Chrome driver (specify the path to chromedriver if necessary)
service = Service()
chrome_driver = webdriver.Chrome(service=service)

try:
    # Open the website
    chrome_driver.get("https://www.globalsqa.com/")

    # Maximize the browser window
    chrome_driver.maximize_window()
    time.sleep(2)  # Adding a delay to ensure the page is fully loaded

    # ID Locator - Unique
    search_box = chrome_driver.find_element(By.ID, "s")
    search_box.send_keys("Python")
    time.sleep(1)

    # CLASS Locator - Not Unique
    search_button = chrome_driver.find_element(By.CLASS_NAME, "button_search")
    search_button.click()
    time.sleep(2)

    # Correct TAG Locator usage - Not Unique
    # Using `find_elements` to get all elements with tag 'a'
    links = chrome_driver.find_elements(By.TAG_NAME, "a")
    print(f"Number of links found: {len(links)}")

    # Link Text Locator
    try:
        cheatsheets_link = chrome_driver.find_element(By.LINK_TEXT, "CHEATSHEETS")
        cheatsheets_link.click()
        time.sleep(2)
    except Exception as e:
        print("Error locating 'CheatSheets' link:", e)

    # Partial Link Text Locator
    try:
        free_link = chrome_driver.find_element(By.PARTIAL_LINK_TEXT, "FREE")
        free_link.click()
        time.sleep(2)
    except Exception as e:
        print("Error locating link with partial text 'Free':", e)

except Exception as e:
    print(f"An error occurred: {e}")


# Optional sleep to view the final page before closing
time.sleep(110)

# Close the browser after tasks are completed
chrome_driver.quit()
