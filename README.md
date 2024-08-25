# Python Automation (Selenium) Testing Scripts

## Test Case - 1: Selenium Login Test
This repository contains a Selenium test script for automating the login process on the OrangeHRM demo website. The script performs the following actions:
1. Opens the OrangeHRM login page.
2. Waits for the username field to be present.
3. Enters the username and password.
4. Clicks the login button.
5. Waits for the title of the page to be "OrangeHRM".
6. Verifies the page title and prints whether the login test passed or failed.
7. Keeps the browser open for 50 seconds to allow manual inspection.
8. Closes the browser after the delay.

## Prerequisites
Before running the test, ensure you have the following installed:
* Python 3.x
* Google Chrome
* ChromeDriver matching your Chrome version

## Installation
* Clone the Repository: `git clone https://github.com/Bhuvneshjai/Automation-Testing-Python.git`
* Navigate to the Project Directory
* Set Up a Virtual Environment: `python -m venv venv`
* Activate the Virtual Environment: `Activate the Virtual Environment`
* Install Required Packages: `pip install selenium`

## Configuration
* Download ChromeDriver
  * Ensure chromedriver.exe is downloaded
  * Update the path in the script if necessary

## Running the Test
`python Test_Case_1.py`

## Script Details
* Import Statements: Imports necessary modules from selenium and time.
* Service Setup: Specifies the path to the ChromeDriver executable.
* Browser Initialization: Initializes the ChromeDriver instance.
* Open Website: Navigates to the OrangeHRM login page.
* Wait for Elements: Uses WebDriverWait to wait for elements to be present.
* Interaction: Fills in username and password, clicks the login button.
* Title Verification: Waits for and verifies the page title.
* Result Output: Prints the result of the login test.
* Browser Management: Keeps the browser open for 50 seconds and then closes it.

## Troubleshooting
* NoSuchElementException: Ensure elements are correctly identified and their locators are accurate.
* TimeoutException: Adjust wait times if elements are not found within the specified time.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
