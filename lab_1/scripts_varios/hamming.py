import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
# Define window type variables for clarity
RECTANGULAR = 'rectangular'
HAMMING = 'hamming'

def get_window(type, length):
    window = list()
    if type == RECTANGULAR:
        for i in range(0, length):
            window.append(1)
    elif type == HAMMING:
        a = 0.53836
        b = 0.46164
        for i in range(0, length):
            window.append(a - b * np.cos(
                (2 * np.pi * i)/(length - 1)))
    return window




def apply_window(signal, window):
    windowed = list()
    for idx, sample in enumerate(signal):
        windowed.append(sample * window[idx])
    return windowed

if __name__ == '__main__':
    audio = AudioSegment.from_file("ruido2.wav")
    signal = np.array(audio.get_array_of_samples())
    window = get_window(HAMMING, len(signal))
    windowed_signal = apply_window(signal, window)


    plt.plot(windowed_signal)
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.show()