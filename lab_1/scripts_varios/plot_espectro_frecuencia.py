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

# Calcular el eje de frecuencia
freqs = np.fft.fftfreq(len(power_spectrum), 1/sample_rate)

# Graficar el espectro de potencia de los datos de audio
plt.figure()
plt.plot(freqs, power_spectrum)
plt.title('Espectro de Frecuencia')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Potencia')

# Mostrar la gráfica
plt.show()
