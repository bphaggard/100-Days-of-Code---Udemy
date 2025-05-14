import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver

class InternetSpeedXBot:
    def __init__(self, promised_down, promised_up, x_email, x_password):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = promised_down
        self.up = promised_up
        self.download = 0.0
        self.upload = 0.0
        self.email = x_email
        self.password = x_password

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)

        # Close popup window
        try:
            popup_button = self.driver.find_element(By.XPATH, value='//*[@id="onetrust-reject-all-handler"]')
            popup_button.click()
            time.sleep(2)
        except NoSuchElementException:
            print("Popup not found or already closed.")

        # Start speed test by clicking Go button
        try:
            start_speed = self.driver.find_element(By.CLASS_NAME, value="start-button")
            start_speed.click()
        except NoSuchElementException:
            print("Go button not found.")
            return

        # Wait till the speed test finishes
        time.sleep(40)

        # Read and show download speed
        try:
            self.download = float(self.driver.find_element(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.download-speed").text)
            print("Download speed:", self.download, "Mbps")
        except NoSuchElementException:
            print("No download speed value found")

        # Read and show upload speed
        try:
            self.upload = float(self.driver.find_element(By.CSS_SELECTOR, ".result-data-large.number.result-data-value.upload-speed").text)
            print("Upload speed:", self.upload, "Mbps")
        except NoSuchElementException:
            print("No upload speed value found")

    def login_to_x(self):
        self.driver.get("https://x.com/")
        time.sleep(2)

        # Sign in button
        try:
            login_button = self.driver.find_element(By.LINK_TEXT, value="Sign in")
            login_button.click()
        except NoSuchElementException:
            print("Sign in button not found.")
            return

        # Fill email
        time.sleep(5)
        login_email = self.driver.find_element(By.CSS_SELECTOR, 'input[name="text"][autocomplete="username"]')
        login_email.send_keys(self.email)
        time.sleep(1)
        next_button = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
        next_button.click()

        # Fill password
        time.sleep(2)
        login_password = self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"][autocomplete="current-password"]')
        login_password.send_keys(self.password)
        time.sleep(1)
        log_in_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div/span/span')
        log_in_button.click()

    def tweet_at_provider(self):
        # message: Hey Internet Provider, why is my internet speed self.download/self.upload when I pay for 100/100?
        pass