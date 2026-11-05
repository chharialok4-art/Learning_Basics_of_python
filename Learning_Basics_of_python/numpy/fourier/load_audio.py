import librosa
import numpy as np
import matplotlib.pyplot as plt

# Load audio
audio, sr = librosa.load("numpy/fourier/music001.mp3", sr=None)

print("Audio samples:", audio)
print("Sampling rate:", sr)
print("Total samples:", len(audio))