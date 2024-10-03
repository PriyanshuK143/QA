from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Navigate to the login page
    driver.get("index.html")  
    
    # Locate the username and password fields
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    # Input valid credentials
    username_field.send_keys("testuser")  # Replace with a valid username
    password_field.send_keys("password123")  # Replace with a valid password

    # Submit the form
    password_field.send_keys(Keys.RETURN)

    # Wait for some time to let the page load
    time.sleep(2)

    # Check for a successful login, e.g., by checking an alert
    alert_text = driver.switch_to.alert.text
    assert "Login successful!" in alert_text  
    driver.switch_to.alert.accept()  # Close the alert

finally:
    # Close the browser
    driver.quit()
