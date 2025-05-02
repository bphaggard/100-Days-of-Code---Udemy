from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Patrick")
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("McCall")
email = driver.find_element(By.NAME, value="email")
email.send_keys("pkMcl@email.com")
button = driver.find_element(By.CSS_SELECTOR, value="form button")
button.click()