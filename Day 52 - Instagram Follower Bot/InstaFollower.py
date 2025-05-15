import time
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstaFollower:

    def __init__(self, insta_email, insta_password):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.email = insta_email
        self.password = insta_password

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(2)

        # Close popup window
        try:
            cookies_popup = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')
            cookies_popup.click()
        except NoSuchElementException:
            print("Popup not found or already closed")

        # Fill email
        time.sleep(2)
        login_email = self.driver.find_element(By.NAME, 'username')
        login_email.send_keys(self.email)
        time.sleep(1)

        # Fill password
        login_password = self.driver.find_element(By.NAME, 'password')
        login_password.send_keys(self.password)
        time.sleep(1)

        # Login button
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/button/div')
        login_button.click()

        # Login info popup
        try:
            not_now_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//div[text()="Not now" and @role="button"]'))
            )
            not_now_button.click()
            print("Clicked 'Not now' successfully")
        except TimeoutException:
            print("The 'Not now' button did not appear or could not be clicked.")

    def find_followers(self):
        pass

    def follow(self):
        pass