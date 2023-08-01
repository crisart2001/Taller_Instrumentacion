import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, ifft
from pydub import AudioSegment

audio = AudioSegment.from_file('file.m4a')
samples = np.array(audio.get_array_of_samples())

# Get the frame rate (samples per second) of the audio
frame_rate = audio.frame_rate

# Calculate the time values for each sample
time = np.arange(len(samples)) / float(frame_rate)

# Plot the audio waveform
plt.figure(figsize=(10, 4))
plt.plot(time, samples)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Signal in Time Domain')
plt.grid()

x = samples
X = fft(x)
N = len(X)
n = np.arange(N)
T = N/frame_rate
freq = n/T 

plt.figure(figsize = (12, 6))
plt.subplot(121)

plt.stem(freq, np.abs(X), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('FFT Amplitude |X(freq)|')
plt.xlim(0, 10)

plt.subplot(122)
plt.plot(time, ifft(X), 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.tight_layout()

plt.show()