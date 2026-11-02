import numpy as np
fs = 100  # Sampling rate: 100 samples per second
duration = 1
t = np.arange(0, duration, 1/fs)
print(np.fft.fft(t[:5]))
print("------------------------------------------------")
print(t[:10])
print("------------------------------------------------")
print(np.fft.fftfreq(8,1))
print("------------------------------------------------")
print(len(t))
print(np.arange(0, 0.05, 0.01))