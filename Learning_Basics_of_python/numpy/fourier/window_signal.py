import numpy as np
import matplotlib.pyplot as plt
sampling_rate = 100
duration = 1

t = np.arange(0,duration,1/sampling_rate)
frequency = 5.5

signal = np.sin(2 * np.pi * frequency * t)
window = np.hanning(len(signal))

windowed_signal = signal * window
fft_original = np.fft.rfft(signal)

fft_windowed = np.fft.rfft(windowed_signal)
freq = np.fft.rfftfreq(len(signal),d=1/sampling_rate)

mag_original = np.abs(fft_original)
mag_windowed = np.abs(fft_windowed)

figure,axis=plt.subplots(2,1,figsize=(8,6))
axis[0].plot(freq,mag_original)
axis[0].set_title("Frequency Normal")
axis[0].set_xlabel("frequency")
axis[0].set_ylabel("magnitude")
axis[0].grid()
axis[1].plot(freq,mag_windowed)
axis[1].set_title("Frequency Normal")
axis[1].set_xlabel("frequency")
axis[1].set_ylabel("window")
axis[0].grid()
plt.show()
