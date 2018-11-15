'''Use spotify API to download 30s previews and song informations'''
import os
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import requests


def download_mp3_from_url(url, dir):
    '''Downloads mp3 file located at given url into given directory'''
    r = requests.get(url)
    open(os.path.join(dir, "song.mp3"), 'wb').write(r.content)

existing_songs_path = ""
#existing_songs = json.loads(open(existing_songs_path).read())  #Dictionary of dictionaries

username = "leafsmaple"
client_id = "76a157b70b5c4e21b1d1c1e8af629db8"
client_secret = "621a656e04e94a6d932ad646fef2f485"

#token = util.prompt_for_user_token(username)
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
cache_token = client_credentials_manager.get_access_token()

playlist_urls = {'rap': "3LFHhtxgV1bpsJV0SLYfPl",
                 'rock': "4n5pu9jboAXAKZFEQvQEgY"}

if cache_token:
    sp = spotipy.Spotify(cache_token)
    sp.trace = False

    for plist in playlist_urls:
        playlist_tracks = sp.user_playlist_tracks(username, playlist_urls[plist], fields="items(track(name,href,album(name,href), external_urls, id))")  #The track we want to deal with has preview link at external_urls field
        metadata = {}
        for track in playlist_tracks['items']:
            metadata[track['track']['id']] = {}
            metadata[track['track']['id']]["name"] = track['track']['name']
            metadata[track['track']['id']]["album"] = track['track']['album']
            metadata[track['track']['id']]["prev"] = track['track']['external_urls']
            metadata[track['track']['id']]["genre"] = plist
        
else:
    print ("Can't get token for", username)