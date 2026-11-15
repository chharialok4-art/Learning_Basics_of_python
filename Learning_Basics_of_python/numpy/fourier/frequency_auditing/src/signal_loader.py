import librosa as lb
from src.frequency_analyser import analyse_sound
def load_sound(audio_123):
    audio,sr=lb.load(audio_123,sr=None)
    audio_frequency,sampling_frequency=analyse_sound(audio,sr)
    return audio_frequency,sampling_frequency