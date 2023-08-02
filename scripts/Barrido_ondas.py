import numpy as np
from scipy import signal
import soundfile as sf
import matplotlib.pyplot as plt

# Parámetros de la señal
duracion = 6 # Duración en segundos
fs = 44100 # Frecuencia de muestreo
frecuencia_inicial = 5000 # Frecuencia inicial en Hz
frecuencia_final = 5000 # Frecuencia final en Hz
tipo_onda = 'senoidal' # Tipo de onda: 'senoidal', 'cuadrada', 'triangular', 'diente de sierra' o 'cosenoidal'

# Generar la señal
t = np.linspace(0, duracion, int(duracion*fs))
frecuencia = np.linspace(frecuencia_inicial, frecuencia_final, int(duracion*fs))

if tipo_onda == 'senoidal':
    senal = np.sin(2*np.pi*frecuencia*t)
elif tipo_onda == 'cuadrada':
    senal = signal.square(2*np.pi*frecuencia*t)
elif tipo_onda == 'triangular':
    senal = signal.sawtooth(2*np.pi*frecuencia*t, 0.5)
elif tipo_onda == 'diente de sierra':
    senal = signal.sawtooth(2*np.pi*frecuencia*t)
elif tipo_onda == 'cosenoidal':
    senal = np.cos(2*np.pi*frecuencia*t)

# Guardar la señal en un archivo WAV
sf.write('senoidal_5k.wav', senal, fs)

print('Señal guardada en "senal.wav"')

# Graficar la señal
plt.plot(t, senal)
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.show()