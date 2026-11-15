import numpy as np
import matplotlib as mltb
import librosa as lb
from pathlib import Path
from src.signal_loader import load_sound
from src.visulization import show_business
BASE_PATH=Path(__file__).resolve().parent
audio_path=BASE_PATH/"data"/"audio"/"sound_123.mp3"
audio_frequency,sampling_frequency=load_sound(audio_path)
print("\n\n\n")
print("audio_frequency:",audio_frequency,"\n",)
print("\n\n\n")
print("sampling_frequency",sampling_frequency)
show_business(audio_frequency,sampling_frequency)