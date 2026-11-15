import numpy as np
def signal_analyser(audio,sr):
    rfft_value=np.fft.rfft(audio)
    frequency=np.fft.rfftfreq(len(audio),1/sr)
    return np.abs(rfft_value),frequency