import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from scipy.signal import butter, sosfiltfilt
frequency=500
duration=2
time=np.arange(0,duration,1/frequency)
signal=np.sin(2*np.pi*10*time)
noise=np.random.normal(0,0.3,len(signal))
noisy_signal=signal+noise
sos = butter(10,20,btype="lowpass",fs=frequency,output="sos")
filtered_signal = sosfiltfilt(sos, noisy_signal)
print(len(noise))
plt.plot(sos)
plt.show()
# sd.play(signal,frequency)
# sd.wait()