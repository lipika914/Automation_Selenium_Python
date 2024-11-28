Selenium-Based Data-Driven Testing with Python
This repository demonstrates two approaches to data-driven testing using Selenium and Python. It includes examples of testing with both hardcoded data and external JSON files to suit various scenarios.

Project Structure
The repository contains the following files:

ddt_hard_code.py
A basic Selenium test script with hardcoded data.

Suitable for simple, static test cases.
Demonstrates browser automation, element interactions, and result validation.

ddt_json_data.py:
A dynamic Selenium test script driven by JSON data.

Separates test data from the logic for better maintainability and scalability.
Reads structured data from a JSON file to execute multiple test cases.
Tools and Technologies
Python: The primary language for writing test scripts.
Selenium: A powerful tool for browser automation and web testing.
JSON: Used as a data format for dynamic test case input in ddt_json_data.py.
How to Use
Prerequisites
Install Python:
Make sure Python 3.7+ is installed on your system.
Download Python

Install Selenium:
Use pip to install Selenium:

bash
Copy code
pip install selenium
Download a WebDriver:
Download the WebDriver (e.g., ChromeDriver) for your preferred browser.
Download ChromeDriver

Clone the Repository:
Clone this repository to your local machine:


json
Copy code
[
    {"username": "rahulshettyacademy", "password": "learning", "should_succeed": true},
    {"username": "invalidUser", "password": "invalidPass", "should_succeed": false}
]
Run the script:

bash
Copy code
python ddt_json_data.py
Key Features
Hardcoded Tests: Quick and simple for static test scenarios.
JSON-Driven Tests: Scalable and maintainable by decoupling test data from the test logic.
Selenium Automation: Browser automation to test web applications.
