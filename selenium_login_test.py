import time
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"{username}@{domain}.com"

def generate_random_password():
    return ''.join(random.choices(string.ascii_letters + string.digits + "!@#$", k=12))

def main():
    # Set up Chrome options
    options = Options()
    # If you want to run it headless, uncomment the line below:
    # options.add_argument('--headless')
    
    # Initialize the Chrome webdriver
    print("Launching Chrome browser...")
    driver = webdriver.Chrome(options=options)
    
    try:
        # Navigate to the Laravel login page
        url = "http://da.adlynk.in.test/"
        print(f"Navigating to {url}...")
        driver.get(url)
        
        # Wait a moment for page load
        time.sleep(3)
        
        # Locate the email and password fields
        email_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")
        
        # Generate random values
        random_email = generate_random_email()
        random_password = generate_random_password()
        
        print(f"Entering email: {random_email}")
        email_field.send_keys(random_email)
        time.sleep(1)
        
        print(f"Entering password: [hidden]")
        password_field.send_keys(random_password)
        time.sleep(2)
        
        # Optionally locate and submit the form or click login
        # login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        # login_button.click()
        # time.sleep(3)
        
        print("Fields successfully automated. Closing browser in 3 seconds...")
        time.sleep(3)
        
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Close the browser session
        driver.quit()
        print("Browser closed. Exiting.")

if __name__ == "__main__":
    main()
