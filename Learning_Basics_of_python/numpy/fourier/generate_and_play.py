import numpy as np
import sounddevice as sd
frequency=18000
sample_rate=44100
time=np.arange(0,4,1/sample_rate)
signal=np.sin(2*np.pi*frequency*time)
sd.play(signal,sample_rate)
sd.wait()