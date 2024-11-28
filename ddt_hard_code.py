import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@ddt
class LoginTestDDT(unittest.TestCase):
 def setUp(self):
# Initialize the WebDriver
  self.driver = webdriver.Chrome()
  self.driver.maximize_window()
  self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")

 def tearDown(self):
# Close the WebDriver after each test
  self.driver.quit()
 @data(
("rahulshettyacademy", "learning", True),
        ("invalid_username", "valid_password", False),
        ("valid_username", "invalid_password", False),
        ("", "", False)
 )
 @unpack
 def test_login(self, username, password, should_succeed):
   try:
     username_field = WebDriverWait(self.driver, 10).until(
     EC.presence_of_element_located((By.ID, 'username')))
     password_field = self.driver.find_element(By.ID, 'password')
     singin = self.driver.find_element(By.XPATH, "//input[@name='signin']")
     username_field.send_keys(username)
     password_field.send_keys(password)
     singin.click()

     if should_succeed:
         checkout_button = WebDriverWait(self.driver, 10).until(
             EC.presence_of_element_located((By.XPATH, "//li[@class='nav-item active']")))

         self.assertTrue(checkout_button.is_displayed(), "Login assertion failed for valid credentials.")
         print("Login successful and validated!")
     else:
         error_element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,'error-message')))

         self.assertTrue(error_element.is_displayed(), "Error message not displayed for invalid credentials.")
         print("Login failed as expected with invalid credentials.")
   except TimeoutException:
    if should_succeed:
       self.fail("Login failed or timed out unexpectedly for valid credentials.")
       # Run the tests


if __name__ == "__main__":
           unittest.main()