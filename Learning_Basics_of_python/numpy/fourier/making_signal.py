import numpy as np
import matplotlib.pyplot as plt
sample_frequency=100;
duration=1 

t=np.arange(0,duration,1/sample_frequency)
signal= np.sin(2*np.pi*5*t)

signal_fft = np.fft.fft(signal)
signal_absolute = np.abs(signal_fft)
signal_frequency = np.fft.fftfreq(len(signal),1/sample_frequency)
print("Sine Wave Signal",signal[0:10])
print("-------------------------------------------------------------------------")
print("fft signal",signal_fft[0:10])
plt.plot(t,signal,label="Sin wawe")
plt.show()
plt.plot(signal_frequency,signal_absolute,label="fft signal")
plt.show()
