import os
import librosa
import torch
import numpy as np


base_path = os.path.dirname(os.path.realpath(__file__))
songsdir_path = os.path.join(base_path,"songs")
rock_path = os.path.join(songsdir_path, "rock")
rap_path = os.path.join(songsdir_path, "rap")
assert os.path.isdir(songsdir_path)



for song_path in os.listdir(rock_path):
    song_path = os.path.join(rock_path, song_path)
    y, sr = librosa.load(song_path)
    try :
        rock_array = np.concatenate(rock_array, y, 1)
    except NameError:
        rock_array = y
    except :
        if y.shape > rock_array.shape[1]:
            y = y[:rock_array.shape[1]]
        else:
            y = np.pad(y, rock_array.shape[1] - y.shape,"constant")
        rock_array = np.concatenate(rock_array, y, 1)
np.savetxt("rock_songs.csv", rock_array, delimiter=",")



# for song_path in os.listdir(rap_path):
#     song_path = os.path.join(rap_path, song_path)
#     y, sr = librosa.load(song_path)
#     if rap_array == []:
#         rap_array = y
#     else:
#         rap_array = np.concatenate(rap_array, y, 1)
# np.savetxt("rap_songs.csv", rock_array, delimiter=",")
