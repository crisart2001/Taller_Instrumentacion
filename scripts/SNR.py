import numpy as np
from scipy.io import wavfile
from scipy.fftpack import fft
import matplotlib.pyplot as plt

# Leer el archivo de audio
sample_rate, data = wavfile.read('senoidal_5-5k.wav')

# Calcular la FFT de los datos de audio
fft_data = fft(data)

# Calcular el espectro de potencia de los datos de audio
power_spectrum = np.abs(fft_data) ** 2

# Estimar la potencia del ruido promediando el espectro de potencia en un rango de frecuencia donde solo hay ruido presente
noise_start = 0
noise_end = 1000

noise_power = np.mean(power_spectrum[noise_start:noise_end])

# Estimar la potencia de la señal restando la potencia del ruido del poder total
signal_power = np.sum(power_spectrum) - noise_power

# Calcular el SNR en decibelios
snr = 10 * np.log10(signal_power / noise_power)

# Graficar el espectro de potencia de los datos de audio
plt.figure()
plt.plot(power_spectrum)
plt.title('Espectro de Potencia')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Potencia')

# Graficar el SNR como una línea horizontal en la misma gráfica
plt.axhline(y=snr, color='r', linestyle='--')
plt.legend(['Espectro de Potencia', 'SNR'])

# Mostrar la gráfica
plt.show()
