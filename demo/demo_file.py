import os
import torch
import librosa
import json
import numpy as np

def get_normalized_sample(song_path):
    '''Take in path to song return numpy array of sample'''
    y, sr = librosa.load(song_path)

    # Take 2 samples of length 200,000 (roughly 10 seconds) from each song, spaced evenly apart
    start = int(1 * y.shape[0] / 2)
    end = start + 200000
    return y[start:end]

def mmfc_transform(song_array):
    return song_array

def run_demo():
    '''Launch command line demo that prompts user to input song, plays it back, and then predicts'''

    while True:
        mp3_path = input('Enter the name of your song (artist_title) \n')
        mp3_path = os.path.join("demo_songs", mp3_path + ".mp3")

        song_array = get_normalized_sample(mp3_path)
        transformed_song_array = mmfc_transform(song_array)
        model = torch.load("model.pt")
        results = model.predict(song_array)

        num_to_label = json.load("num_to_label.json")
        confidence = []
        for i in range (0, len(results)):
            confidence.append(num_to_label[results[i]])

        for i in range(0, len(results)):
            print(str(num_to_label[i]), " :", confidence[i], " -- ")
        print ('\n')