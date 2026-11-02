import numpy as np
from scipy.signal import find_peaks
import matplotlib.pyplot as plt
sampling_rate = 500
duration = 2
t = np.arange(0, duration, 1/sampling_rate)
signal = (3*np.sin(2*np.pi*5*t) + 2*np.sin(2*np.pi*15*t) + 1*np.sin(2*np.pi*30*t))
fft_values = np.fft.rfft(signal)
frequencies = np.fft.rfftfreq(len(signal), d=1/sampling_rate)
magnitude = np.abs(fft_values)
peaks, properties = find_peaks(magnitude)
detected_frequencies = frequencies[peaks]
detected_magnitudes = magnitude[peaks]
for freq, mag in zip(detected_frequencies,detected_magnitudes):
    if mag > 100:
        print(freq, mag)
print("Signal:-",fft_values[:10])
print("\n")
print("Frequencies:-",frequencies[:10])
print("\n")
print("Magnitude:-",magnitude[:10])
