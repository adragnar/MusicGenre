import librosa
import sounddevice as sp


y, sr = librosa.load("test.mp3")

# Take 2 samples of length 200,000 (roughly 10 seconds) from each song, spaced evenly apart
# start = int(1 * y.shape[0] / 2)
# end = start + 200000
# y = y[start:end]


sp.play(y, 22050)
print(3)