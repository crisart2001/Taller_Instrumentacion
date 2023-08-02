import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft
from pydub import AudioSegment

#audio = AudioSegment.from_file('file.m4a')
audio = AudioSegment.from_file('senoidal_5-5k.wav')
samples = np.array(audio.get_array_of_samples())
print(len(samples))

frame_rate = audio.frame_rate
time = np.arange(len(samples)) / float(frame_rate)

bin_size = 1024
num_bins = len(samples) // bin_size

bins = np.array_split(samples, num_bins)

last_bin_size = len(bins[-1])
if last_bin_size < bin_size:
    bins.pop()  # Remove the last bin if it's too small
    last_bin_padded = np.pad(samples[-last_bin_size:], (0, bin_size - last_bin_size), 'constant')
    bins.append(last_bin_padded)

x = samples
X = fft(x)
N = len(X)
n = np.arange(N)
T = N/frame_rate
freq = n/T 


plt.figure(figsize=(10, 4))
plt.plot(time, samples)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Signal in Time Domain')
plt.grid()

plt.figure(figsize = (12, 6))
plt.subplot(121)

plt.stem(freq, np.abs(X), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(0, 10)
plt.yscale('log')

plt.subplot(122)
plt.plot(time, ifft(X), 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()

plt.show()