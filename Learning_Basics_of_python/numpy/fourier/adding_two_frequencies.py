import numpy as np
import matplotlib.pyplot as plt
f1 = 5
f2 = 15
fs = 100
duration = 1
t = np.arange(0, duration, 1/fs)
signal1 = np.sin(2 * np.pi * f1 * t)
signal2 = np.sin(2 * np.pi * f2 * t)
signal = signal1 + signal2
cal_fft = np.fft.fft(signal[:10]);
print("FFT:-",cal_fft);
plt.plot(t, signal)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Combined Signal: 5 Hz + 15 Hz")
plt.grid()
plt.show()