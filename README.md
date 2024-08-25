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

### Prerequisites
Before running the test, ensure you have the following installed:
* Python 3.x
* Google Chrome
* ChromeDriver matching your Chrome version

### Installation
* Clone the Repository: `git clone https://github.com/Bhuvneshjai/Automation-Testing-Python.git`
* Navigate to the Project Directory
* Set Up a Virtual Environment: `python -m venv venv`
* Activate the Virtual Environment: `Activate the Virtual Environment`
* Install Required Packages: `pip install selenium`

### Configuration
* Download ChromeDriver
  * Ensure chromedriver.exe is downloaded
  * Update the path in the script if necessary

### Running the Test
`python Test_Case_1.py`

### Script Details
* Import Statements: Imports necessary modules from selenium and time.
* Service Setup: Specifies the path to the ChromeDriver executable.
* Browser Initialization: Initializes the ChromeDriver instance.
* Open Website: Navigates to the OrangeHRM login page.
* Wait for Elements: Uses WebDriverWait to wait for elements to be present.
* Interaction: Fills in username and password, clicks the login button.
* Title Verification: Waits for and verifies the page title.
* Result Output: Prints the result of the login test.
* Browser Management: Keeps the browser open for 50 seconds and then closes it.

### Troubleshooting
* NoSuchElementException: Ensure elements are correctly identified and their locators are accurate.
* TimeoutException: Adjust wait times if elements are not found within the specified time.

## Test Case - 2: Selenium Login Test
This test case is designed to automate the login process for the nopCommerce admin demo site using Selenium WebDriver with the Microsoft Edge browser. The test verifies whether the login process is successful by checking the page title after logging in.

### Prerequisites
- Python 3.x installed on your system.
- Selenium WebDriver installed (`pip install selenium`).
- Microsoft Edge browser installed.
- Microsoft Edge WebDriver downloaded and set up correctly.

### Setup Instructions
1. **Install Selenium**:
   Make sure you have Selenium installed. You can install it using pip:
   ```bash
   pip install selenium

2. **Download Microsoft Edge WebDriver:** Download the appropriate version of the Edge WebDriver that matches your installed version of Microsoft Edge.
3. **Set the Path for Edge WebDriver:** Ensure the path to the Edge WebDriver executable (msedgedriver.exe) is correctly specified in the script.

This test case performs the following steps:
1. Open the nopCommerce Admin Demo Login Page:
   * URL: https://admin-demo.nopcommerce.com/login
2. Wait for the Login Page to Load:
   * The script waits for the "Email" input field to be present.
3. Enter Login Credentials:
    * The email and password fields are filled in with the appropriate credentials (currently left blank in the script).
4. Click the Login Button:
    * The script clicks the "Login" button to attempt to log in.
5. Check the Page Title After Login:
    * After the login attempt, the script checks the page title.
    * The expected title is "Dashboard / nopCommerce administration".
    * If the title matches, the login is considered successful; otherwise, it fails.
6. Keep the Browser Open for 50 Seconds:
   * The browser window remains open for 50 seconds after the test for manual inspection, then closes automatically.
   
### How to Run the Test
1. Clone this repository to your local machine.
2. Ensure you have set up the virtual environment (optional) and installed the required dependencies.
3. Run the test script using Python:
   ```bash
   python "path_to_your_script/Test Case - 2.py"
### Expected Output
* If the login is successful, the console will print:
  ```
   Login Passed
* If the login fails (e.g., due to an incorrect title), the console will print:
  ```
   Login Failed
### Troubleshooting
* If the script throws a TimeoutException, it might be due to the CAPTCHA check. In such cases, manually solve the CAPTCHA and then proceed with the test.
* Ensure the Edge WebDriver version matches your installed Edge browser version.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
