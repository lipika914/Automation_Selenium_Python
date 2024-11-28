import json
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginTestDDT(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        #self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    def tearDown(self):
        # Quit the WebDriver
        self.driver.quit()


    def test_login_from_json(self):

        # Load test data

        with open('dataset.json', 'r') as file:
            data = json.load(file)
            for entry in data:


             try:
               self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")
               username = entry['username']
               password = entry['password']
               should_succeed = entry['should_succeed']

               username_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'username')))
               password_field = self.driver.find_element(By.ID, 'password')
               signin_button = self.driver.find_element(By.XPATH, "//input[@name='signin']")


               username_field.clear()
               password_field.clear()
               username_field.send_keys(username)
               password_field.send_keys(password)
               signin_button.click()

               if should_succeed:
                    checkout_button = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//li[@class='nav-item active']")))

                    self.assertTrue(checkout_button.is_displayed(), "Login assertion failed for valid credentials.")
                    print("Login successful and validated!")
               else:
                    error_element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, 'error-message')))

                    self.assertTrue(error_element.is_displayed(),
                                    "Error message not displayed for invalid credentials.")
                    print("Login failed as expected with invalid credentials.")
             except TimeoutException:
              if should_succeed:
                    self.fail("Login failed or timed out unexpectedly for valid credentials.")
                    # Run the tests


if __name__ == "__main__":
    unittest.main()
