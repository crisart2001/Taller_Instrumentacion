import numpy as np
from scipy.signal import freqz
from scipy.io import wavfile
from scipy import signal
import matplotlib.pyplot as plt

frecuencia_muestreo, senal = wavfile.read('ruido2.wav')
Fs = frecuencia_muestreo
N=len(senal)
Ts=1.0/Fs
t= np.linspace(0.0,N*Ts,N)

plt.figure()
plt.plot(t,senal)
plt.title('Senal de entrada')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')

N=10
frecuencia=0.2
pasa_bajas=signal.firwin(N,frecuencia,pass_zero=True)
x_LPF=signal.lfilter(pasa_bajas,[1.0],senal)
ganancia_LPF=0.4
lpf=ganancia_LPF*x_LPF

frecuencia=[0.20,0.50]
pasa_banda=signal.firwin(N,frecuencia,pass_zero=False)
x_BPF=signal.lfilter(pasa_banda,[1.0],senal)
ganancia_BPF=1.5
bpf=ganancia_BPF*x_BPF

frecuencia=0.40
pasa_altas=signal.firwin(N+1,frecuencia,pass_zero=False)
x_HPF=signal.lfilter(pasa_altas,[1.0],senal)
ganancia_HPF=0.2
hpf=ganancia_HPF*x_HPF

senal_ecualizada=lpf+bpf+hpf

wavfile.write('senal_ecualizada.wav', frecuencia_muestreo, senal_ecualizada.astype(np.int16))

plt.figure()
plt.plot(t,senal_ecualizada.astype(np.int16))
plt.title('Senal ecualizada')
plt.xlabel('Tiempo')
plt.ylabel('Amplitud')

plt.show()