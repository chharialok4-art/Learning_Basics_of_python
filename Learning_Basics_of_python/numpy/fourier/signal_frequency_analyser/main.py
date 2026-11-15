import numpy as np
import pandas as pd
import librosa as lib
from pathlib import Path
from src.frequency_analyser import signal_analyser
from src.signal_loader import load_sound
BASE_DIR=Path(__file__).resolve().parent
audio_path=BASE_DIR/"data"/"audio"/"sound_123.mp3"
if __name__=="__main__":
    audio,sr=load_sound(audio_path)
    frequency,magnitude=signal_analyser(audio,sr)
    print("Audio:",frequency)
    print("---------------------------------------------------------")
    print("Sampling rate:",magnitude)