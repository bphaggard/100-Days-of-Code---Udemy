import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
title_text = soup.find_all("h3", class_="title")

website_movies = [title.getText() for title in title_text]
movies_list = website_movies[::-1]

for movie in movies_list:
    with open("100_movies.txt", mode="a") as file:
        file.write(f"{movie}\n")