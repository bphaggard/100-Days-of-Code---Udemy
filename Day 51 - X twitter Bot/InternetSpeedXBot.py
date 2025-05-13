import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver

class InternetSpeedXBot:
    def __init__(self, promised_down, promised_up):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = promised_down
        self.up = promised_up
        self.download = 0.0
        self.upload = 0.0

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

    def tweet_at_provider(self):
        pass