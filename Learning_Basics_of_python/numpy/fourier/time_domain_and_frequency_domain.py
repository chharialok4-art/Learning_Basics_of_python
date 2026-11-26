import numpy as np
import matplotlib.pyplot as plt
fs=100
f1=3
f2=5
f3=7
time=np.arange(0,4,1/fs)
signal=np.sin(2*np.pi*f1*time) + np.sin(2*np.pi*f2*time) + np.sin(2*np.pi*f3*time)
rfft_values=np.fft.rfft(signal)
frequency=np.fft.rfftfreq(len(signal),1/fs)
magntude=np.abs(rfft_values)
fig,ax=plt.subplots(2,1, figsize=(8, 6))
spectral_leakage= magntude/len(signal)
spectral_leakage[1:-1] *=2
peak_spectral_leakage_index=np.argmax(spectral_leakage)
print("\n\nMax magnitude:",magntude[peak_spectral_leakage_index])
print("--------------------------------------------------------------------------------------")
print("\n\nMAx frequency:",frequency[peak_spectral_leakage_index])
ax[0].plot(frequency,magntude)
ax[0].set_title("Time Domain Graph")
ax[0].set_xlabel("frequency")
ax[0].set_ylabel("magnitude")
ax[0].grid()
ax[1].plot(time,signal)
ax[1].set_title("Frequency Domain Graph")
ax[1].set_xlabel("time")
ax[1].set_ylabel("signal")
ax[1].grid()
plt.show()

