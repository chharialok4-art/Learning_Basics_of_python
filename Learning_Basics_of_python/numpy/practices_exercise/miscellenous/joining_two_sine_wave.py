import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 1, 1000, endpoint=False)
x1 = np.sin(2 * np.pi * 2 * t)
x2 = np.sin(2 * np.pi * 5 * t)
signal = x1 + x2
print(signal[:5])
print(signal.shape)
plt.plot(t, signal)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Combined Signal")
plt.show()