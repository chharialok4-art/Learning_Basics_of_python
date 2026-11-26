import numpy as np
from src.visulization import plot_graph
def setup_frequency():
    fs=500
    time=np.arange(0,2,1/fs)
    f1=np.sin(2*np.pi*5*time)
    f2=np.sin(2*np.pi*6*time)
    f3=np.sin(2*np.pi*7*time)
    signal=f1+f2+f3
    real_fft_value=np.fft.rfft(signal)
    real_magnitude=np.abs(real_fft_value)
    real_frequency=np.fft.rfftfreq(len(signal),1/fs)

    noise = np.random.normal(0, 0.2, len(time))
    noisy_signal=signal+noise

    real_fft_value_noisy=np.fft.rfft(noisy_signal)
    real_frequency_noisy=np.fft.rfftfreq(len(noisy_signal),1/fs)
    real_magnitude_noisy=np.abs(real_fft_value_noisy)

    index_top=np.argsort(real_magnitude_noisy)[-4:][::-1]
    for item in index_top:
        print(f"frequencies:,{real_frequency_noisy[item]:.2f} Hz")
    print("----------------------------------------------------------------------------------")
    for item in index_top:
        print(f"Magnitude:,{real_magnitude_noisy[item]:.2f}")
    plot_graph(time,signal,real_magnitude_noisy,real_frequency_noisy,noisy_signal)