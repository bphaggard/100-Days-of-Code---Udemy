import os
from dotenv import load_dotenv

PROMISED_DOWN = 100
PROMISED_UP = 100

load_dotenv()
X_EMAIL = os.getenv("X_EMAIL")
X_PASSWORD = os.getenv("X_PASSWORD")