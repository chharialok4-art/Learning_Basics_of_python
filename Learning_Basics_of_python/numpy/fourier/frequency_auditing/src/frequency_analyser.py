import numpy as np
def analyse_sound(audio,sr):
    audio_frequency=np.fft.rfft(audio)
    sampling_frequency=np.fft.rfftfreq(len(audio),1/sr)
    return audio_frequency,sampling_frequency