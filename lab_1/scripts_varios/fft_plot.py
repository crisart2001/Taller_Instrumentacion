import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
from pydub import AudioSegment


def get_window(type, length):
    window = list()
    if type == 'rectangular':
        for i in range(0, length):
            window.append(1)
    elif type == 'hamming':
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

def fft_plot(nombre_audio):
    plt.close('all')
    audio = AudioSegment.from_file("ruido2.wav")
    signal_ = np.array(audio.get_array_of_samples())
    window = get_window('hamming', len(signal_))
    signal = apply_window(signal_, window)

    
    frame_rate = audio.frame_rate
    time = np.arange(len(signal)) / float(frame_rate)
    bin_size = 1024
    num_bins = len(signal) // bin_size
    bins = np.array_split(signal, num_bins)
    fft_bins = [fft(bin) for bin in bins]
    max_size = max([len(bin) for bin in fft_bins])
    fft_bins_padded = [np.pad(bin, (0, max_size - len(bin)), 'constant') for bin in fft_bins]
    fft_sum = np.sum(fft_bins_padded, axis=0)
    frequency = np.fft.fftfreq(max_size, d=1.0/frame_rate)

    plt.figure(figsize=(10, 4))
    plt.plot(time, signal)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('Audio Signal in Time Domain')
    plt.grid()


    plt.figure(figsize=(15, 5))

    # Plot 1: FFT of Audio Signal
    plt.subplot(131)
    plt.plot(frequency, np.abs(fft_sum))
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Summed FFT of Audio Signal')

    # Plot 2: Summed FFT using stem on a semilogarithmic scale
    plt.subplot(132)
    plt.plot(frequency, np.abs(fft_sum))
    plt.semilogy()
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Summed FFT of Audio Signal (Semilog)')

    # Plot 3: Normalized FFT using stem on a semilogarithmic scale
    plt.subplot(133)
    plt.plot(frequency, np.abs(fft_sum) / np.abs(fft_sum))
    plt.semilogy()
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Normalized')

    plt.tight_layout()
    

    power_spectrum = np.abs(fft_sum)**2
    plt.figure()
    plt.plot(frequency, power_spectrum)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Power Spectral Density')
    plt.show()

    return [[frequency], [fft_sum]]
