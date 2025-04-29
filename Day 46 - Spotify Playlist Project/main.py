import requests
import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

time_machine = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{time_machine}"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(BILLBOARD_URL, headers=header)
response.raise_for_status()
url_data = response.text

soup = BeautifulSoup(url_data, "html.parser")
soup_data = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in soup_data]
print(song_names)

# Spotify
scope = "playlist-modify-private"

CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
REDIRECT_URI = "https://example.com"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope="playlist-modify-private",
        cache_path="token.txt"))

user_id = sp.current_user()["id"]
print(user_id)

song_uris = []
year = time_machine.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

my_playlist = sp.user_playlist_create(user=user_id, name=f"{time_machine} Billboard Top Tracks", public=False,
                                      description="Top Tracks from back in the Dayz of Brunel")
sp.playlist_add_items(playlist_id=my_playlist["id"], items=song_uris)