import numpy as np
import matplotlib.pyplot as plt
signal_frequency=5
sampling_frequency=20
duration=1
time_interval=np.arange(0,duration,1/sampling_frequency)
print("Time Interval:-",time_interval);
signal=np.sin(2*np.pi*signal_frequency*time_interval);
print(signal[:10])
plt.stem(time_interval, signal)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Sampled 5 Hz Sine Wave")
plt.grid(True)
plt.show()