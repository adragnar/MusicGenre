import os
import librosa
import torch
import numpy as np

from normalize_data import *

if __name__ == "__main__":
    base_path = os.path.dirname(os.path.realpath(__file__))
    songsdir_path = os.path.join(base_path,"songs")
    rock_path = os.path.join(songsdir_path, "rock")
    rap_path = os.path.join(songsdir_path, "rap")
    assert os.path.isdir(songsdir_path)



    for song_path in os.listdir(rock_path):
        song_path = os.path.join(rock_path, song_path)
        y, sr = librosa.load(song_path)
        try :
            rock_array = np.concatenate((rock_array, y), axis=1)
        except NameError:
            rock_array = np.expand_dims(y, 0)
        except :
            if y.shape[0] > rock_array.shape[1]:
                y = y[:rock_array.shape[1]]
            else:
                y = np.pad(y, (0, rock_array.shape[1] - y.shape[0]),"constant")
            rock_array = np.concatenate((rock_array, np.expand_dims(y, 0)), axis=0)
    np.save("rock_songs.npy", rock_array)



# for song_path in os.listdir(rap_path):
#     song_path = os.path.join(rap_path, song_path)
#     y, sr = librosa.load(song_path)
#     if rap_array == []:
#         rap_array = y
#     else:
#         rap_array = np.concatenate(rap_array, y, 1)
# np.savetxt("rap_songs.csv", rock_array, delimiter=",")
