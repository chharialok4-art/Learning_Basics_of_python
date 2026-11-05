import numpy as np
import matplotlib.pyplot as plt

fs = 100
duration = 1
f = 5

t = np.arange(0, duration, 1/fs)

signal = np.sin(2 * np.pi * f * t)

rfft_result = np.fft.rfft(signal)
fft_result = np.fft.fft(signal)

# Generate frequency values
rfft_freq = np.fft.rfftfreq(len(signal), d=1/fs)
fft_freq = np.fft.fftfreq(len(signal), d=1/fs)

# Calculate magnitude
rfft_magnitude = np.abs(rfft_result)
fft_magnitude = np.abs(fft_result)

plt.plot(rfft_freq, rfft_magnitude, label="RFFT")
plt.plot(fft_freq, fft_magnitude, label="FFT")

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT vs RFFT")
plt.legend()
plt.grid()

plt.show()