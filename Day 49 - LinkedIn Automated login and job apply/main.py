from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# Open LinkedIn Jobs page
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(2)  # Wait for the page and popup to load

try:
    # Find the close (X) button via XPath that matches the specific SVG path
    close_button = driver.find_element(By.XPATH, "//button//*[name()='svg']//*[name()='path' and @d='M20,5.32L13.32,12,20,18.68,18.66,20,12,13.33,5.34,20,4,18.68,10.68,12,4,5.32,5.32,4,12,10.69,18.68,4Z']/ancestor::button")
    close_button.click()
    print("Popup closed.")
except Exception as e:
    print("Popup not found or already closed.", e)

try:
    sign_button = driver.find_element(By.LINK_TEXT, value='Sign in')
    sign_button.click()
except Exception as e:
    print("Sign up button not found", e)

email = driver.find_element(By.ID, value="username")
email.send_keys("test@email.com")
password = driver.find_element(By.ID, value="password")
password.send_keys("123456")
signup_button = driver.find_element(By.CSS_SELECTOR, value="form button")
signup_button.click()