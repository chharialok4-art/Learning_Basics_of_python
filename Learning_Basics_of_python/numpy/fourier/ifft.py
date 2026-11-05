import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 100
duration = 1

t = np.arange(0, duration, 1/sampling_rate)
signal = np.sin(2 * np.pi * 5 * t)

fft_values = np.fft.fft(signal)
reconstructed_signal = np.fft.ifft(fft_values)
reconstructed_signal = reconstructed_signal.real

plt.plot(t, signal, label="Original Signal")
plt.plot(t, reconstructed_signal, "--", label="Reconstructed Signal")

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Original vs Reconstructed Signal")
plt.legend()
plt.grid()
plt.show()