import os
from dotenv import load_dotenv
from InternetSpeedXBot import InternetSpeedXBot

PROMISED_DOWN = 100
PROMISED_UP = 100

load_dotenv()
X_EMAIL = os.getenv("X_EMAIL")
X_PASSWORD = os.getenv("X_PASSWORD")

speed_test = InternetSpeedXBot(PROMISED_DOWN, PROMISED_UP, X_EMAIL, X_PASSWORD)
speed_test.get_internet_speed()
speed_test.login_to_x()