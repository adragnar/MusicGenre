'''Use spotify API to download 30s previews and song informations'''
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import requests


def download_mp3_from_url(url, dir):
    '''Downloads mp3 file located at given url into given directory'''
    r = requests.get(url)
    open(os.path.join(dir, "song.mp3"), 'wb').write(r.content)


username = "leafsmaple"
client_id = "76a157b70b5c4e21b1d1c1e8af629db8"
client_secret = "621a656e04e94a6d932ad646fef2f485"

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)

if client_credentials_manager:
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    sp.trace = False
    #results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
else:
    print ("Can't get token for", username)