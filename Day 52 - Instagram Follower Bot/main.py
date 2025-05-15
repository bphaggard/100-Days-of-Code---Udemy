import os
from dotenv import load_dotenv
from InstaFollower import InstaFollower

load_dotenv()
insta_email = os.getenv("INSTA_EMAIL")
insta_password = os.getenv("INSTA_PASSWORD")

insta_follower_bot = InstaFollower(insta_email, insta_password)
insta_follower_bot.login()