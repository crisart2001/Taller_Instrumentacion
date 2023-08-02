import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft
from pydub import AudioSegment

plt.close('all')
audio = AudioSegment.from_file("ruido2.wav")
samples = np.array(audio.get_array_of_samples())
frame_rate = audio.frame_rate
time = np.arange(len(samples)) / float(frame_rate)
bin_size = 1024
num_bins = len(samples) // bin_size
bins = np.array_split(samples, num_bins)
fft_bins = [fft(bin) for bin in bins]
max_size = max([len(bin) for bin in fft_bins])
fft_bins_padded = [np.pad(bin, (0, max_size - len(bin)), 'constant') for bin in fft_bins]
fft_sum = np.sum(fft_bins_padded, axis=0)
frequency = np.fft.fftfreq(max_size, d=1.0/frame_rate)
print(frequency)


plt.figure()
plt.plot(frequency, np.abs(fft_sum))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Summed FFT of Audio Signal')

# Plot the summed FFT using stem
# plt.figure()
# plt.stem(frequency, np.abs(fft_sum))
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Amplitude')
# plt.title('Summed FFT of Audio Signal')

# Plot the summed FFT using stem on a semilogarithmic scale
plt.figure()
plt.stem(frequency, np.abs(fft_sum)) #/np.abs(fft_sum)
plt.semilogy()
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Summed FFT of Audio Signal')
plt.show()

plt.figure()
plt.stem(frequency, np.abs(fft_sum)/np.abs(fft_sum)) #/np.abs(fft_sum)
plt.semilogy()
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.title('Normalizada')
plt.show()
print(fft_sum)