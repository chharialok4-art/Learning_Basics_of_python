import numpy as np
import librosa as lb
from pathlib import Path
import matplotlib.pyplot as mplib
import sounddevice as sd
current_folder = Path(__file__).parent
audio_file,sr=lb.load(current_folder/"music001.mp3",sr=None)
normalized_audio = audio_file / np.max(np.abs(audio_file))
print("Sample rate:", sr)
print("Audio shape:", audio_file.shape)
print("Duration:", len(audio_file) / sr)
sd.play(audio_file, sr)
sd.wait()
# time = np.arange(len(audio_file))/sr
# mplib.plot(time,audio_file)
# mplib.show()