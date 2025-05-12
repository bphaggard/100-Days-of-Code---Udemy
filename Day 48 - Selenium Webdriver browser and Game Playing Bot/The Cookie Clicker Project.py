import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

while True:
    button = driver.find_element(By.ID, value="cookie")
    button.click()

    cookie_money = driver.find_element(By.ID, value="money")
    cookie_money_value = int(cookie_money.text)

    buy_cursor = driver.find_element(By.ID, value="buyCursor")
    buy_cursor_price = buy_cursor.find_element(By.TAG_NAME, value="b")
    buy_cursor_price_value = int(buy_cursor_price.text.split(" ")[2].replace(",", ""))

    buy_grandMa = driver.find_element(By.ID, value="buyGrandma")
    buy_grandMa_price = buy_grandMa.find_element(By.TAG_NAME, value="b")
    buy_grandMa_price_value = int(buy_grandMa_price.text.split(" ")[2].replace(",", ""))

    if time.time() > timeout:
        cursor_button = driver.find_element(By.ID, value="buyCursor")
        cursor_button.click()

        grandMa_button = driver.find_element(By.ID, value="buyGrandma")
        grandMa_button.click()

        timeout = time.time() + 5  # Reset timer for next check

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break