import librosa
from pathlib import Path
def load_sound(sound_path):
    audio, sr = librosa.load(sound_path, sr=None)
    return audio, sr