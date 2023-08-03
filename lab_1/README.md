# Taller_Instrumentacion

### 1. ¿Cómo se mide el signal-to-noise ratio (SNR) para una señal analógica? Brinde un ejemplo

Para una señal analógica se necesitan las medidas de la señal y del ruido, estos se pueden obtener en términos de decibeles, de amplitud (de tensión o corriente) o de potencia, dependiendo de la configuración del instrumento que se esté utilizando, entonces se pueden utilizar las siguientes ecuaciones dependiendo de la medición para obtener el SNR en dB:
1. Si se miden en decibeles, solamente es necesario restarle la medida del ruido a la medida de la señal:
$$SNR_{dB} = Señal_{dB} - Ruido_{dB}$$
2. Si se mide en términos de potencia se puede obtener de la siguiente manera:
$$SNR_{dB} = 10\cdot log(\frac{potenciaSeñal}{potenciaRuido})$$
3. Si se mide en términos de amplitud:
$$SNR_{dB} = 20\cdot log(\frac{AmplitudSeñal}{AmplitudRuido})$$
Por ejemplo, si se tiene una medición de audio en la cual la señal tiene un valor de amplitud de 10V y después se mide el silencio para obtener solamente la medida del ruido y esta es de 0.3V entonces se puede obtener con la ecuación del SNR de amplitudes de la siguiente forma:
$$SNR_{dB} = 20\cdot log(\frac{10}{0.3})=30.45dB$$
Ahora suponiendo que existe una resistencia de 30 Ohmios, entonces la potencia de esas amplitudes con la ecuación de P=V^2/R son 3.33W para la señal y de 3mW para el ruido, si la medición es en potencia se obtienen esos valores, entonces utilizando la fórmula de potencias del SNR se tiene:
$$SNR_{dB} = 10\cdot log(\frac{3.33}{3\times 10^{-3}})=30.45dB$$
Y por último si dicha señal viene en decibeles como 10log(3.33W)= 5.224dB para la señal y 10log(3mW)=-25.228dB, entonces se utiliza la ecuación de resta:
$$SNR_{dB} = 5.22 - -25.228 =30.45dB$$
 Y como se puede observar en los resultados del ejemplo, aunque todos se hayan podido medir de diferentes formas, al final todos dieron el mismo valor de SNR.

### 2. ¿Cual es el ancho de banda típico para señales de audio? ¿Una señal de audio tiene componente DC?

El ancho de banda típico para señales de audio es de 20Hz a 20kHz. Una señal analógica de audio no tiene componente DC, ya que un componente DC implica una frecuencia de 0Hz lo cual significa que no varía en el tiempo, y como se mencionó anteriormente, las señales de audio abarcan de los 20Hz a los 20kHz, es decir, no tiene componentes que no varíen en el tiempo.

### 3. ¿Cómo afecta el ruido térmico al SNR de una señal analógica? ¿Cuántos dBm tiene el ruido térmico para una impedancia de 50Ω para una señal cuyo BW= 20kHz?

El ruido térmico puede hacer que disminuya el SNR de una señal analógica debido a que se suma a la potencia de ruido, es decir, si crece el ruido, disminuye el SNR. <br>
Suponiendo que la temperatura es la de ambiente, es decir 298K, y con la constantee de Boltzman de $1.38\times 10^{-23}$ entonces el ruido térmico en dBm es:
$$N_{dBm}= 10\cdot log(\frac{kTB}{1\times 10^{-3}}) = 10\cdot log(\frac{1.38\times10^{-23}\cdot 298\cdot 20 000}{1\times 10^{-3}} )= -130.8 dBm$$
La impedancia no es necesaria para calcular la potencia en dBm.

### 4. ¿Qué es ruido de cuantización? ¿Bajo que circunstancias se podría modelar como ruido aditivo?

El ruido de cuantización es un tipo de error que se introduce cuando se convierte una señal analógica en una señal digital. Esto sucede porque la señal digital solo puede tener valores discretos, mientras que la señal analógica puede tener valores continuos [1]. 
Un ejemplo en el que el ruido de cuantización puede ser modelado como ruido aditivo es cuando se cuantifica una señal sinusoidal. En este caso, la relación señal-ruido de cuantización (SQNR) se puede calcular como la relación entre la potencia promedio de la señal y la potencia promedio del ruido de cuantización

### 5. ¿Para una grabación de audio, el piso de ruido de la señal es predominado por el ruido de cuantización o el ruido térmico?

n una grabación de audio, el piso de ruido de la señal puede ser afectado tanto por el ruido de cuantización como por el ruido térmico.

### 6. ¿Cuales son las tasas de muestreo más populares para grabaciones de audio? ¿La cantidad de bits por muestra?

Las tasas de muestreo más comunes para grabaciones de audio son 44.1 kHz y 48 kHz. También hay tasas de muestreo más altas disponibles, como 88.2 kHz, 96 kHz y 192 kHz. En cuanto a la cantidad de bits por muestra son de 16 bits y 24 bits.


### 7. ¿Cuales son los formatos de audio cuya compresión o almacenamiento no agrega distorsión?
Cuando se trata de analizar los efectos de la compresión con pérdidas uno de estos es la distorsión, sin embargo si se quiere mantener la integridad de la señal original sin ningún tipo de pérdidas se pueden hacer uso de los formatos de compresión sin pérdidas con la única desventaja de tender a ser archivos de mayor tamaño. Los formatos sin pérdidas en la actualidad son:[2]
1. ALAC: desarrollado por Apple con una resolución entre 16-bit/44.1 kHz (calidad de un disco) y 24-bit/192 kHz. Es importante notar que a pesar de que se use ese algoritmo de codificación la extensión de los archivos no es .alac en cambio podría parecer ser de formatos con pérdidas como .m4a no obstante estos son usados solo como contenedores pero el archivo sin pérdidas se encuentran dentro.
2. FLAC: este formato de compresión sin pérdida admite frecuencias de muestreo de alta resolución, ocupa aproximadamente la mitad del espacio de un archivo WAV y almacena metadatos. Este es de fuente libre por lo que es gratis, además, se considera el formato preferido para descargar y almacenar álbumes de alta resolución.
3. MQA: es un formato que utiliza técnicas con y sin pérdidas, sin embargo, este es considerado audiblemente sin pérdidas. Por medio de esta técnica genera archivos de menor tamaño por lo que es óptimo para plataformas de "streaming" o transmisión.
4. WMA lossless: es un formato sin pérdidas propuesto para "Windows Media Audio", sin embargo, en la actualidad ya no es utilizado y mucho teléfonos no son compatibles con susodicho.
### 8. ¿Cómo se puede utilizar un barrido de frecuencias para modelar la respuesta en frecuencia de un dispositivo bajo prueba (DUT)? Investigue el procedimiento a realizar a cada grabación de audio para tener la estimación de la respuesta en frecuencia.
Para modelar la respuesta en frecuencia de un DUT se pueden seguir los siguientes pasos:
1. Generación del audio: es necesario generar un archivo de audio que realice el barrrido de 50Hz hasta 5kHz.
2. Configuración del equipo: para esto se debe disponer del archivo antes generado y se debe preparar tanto un micrófono como un parlante ecualizado para poder realizar la medición. El micrófono debe estar configurado para una codificación sin pérdidas.
3. Medición: para la medición el micrófono y el parlante debe estar a una distancia corta medida y se debe empezar a grabar apenas empieza el parlante a emitir la señal.
4. Análisis de grabaciones: una vez se obtenga el audio grabado, este debe ser transferido a la computadora para ser procesado, el cual debe ser expuesto a una ventana de Hamming y luego a una transformada de Fourier rápida así se obtendría el espectro en frecuencia de dicha señal.
5. Presentación de resultados: a partir de los datos obtenidos después del proceso de la transformada de Fourier se pueden graficar de forma semilogarítmica por medio de alguna biblioteca en python como matplotlib.



Referencias:

[1] B. Widrow & I. Kollár , "Quantization Noise: Roundoff Error in Digital Computation, Signal Processing, Control, and Communications," Published 2008, Cambridge University Press. 

[2] B. Scarrott, "MP3, AAC, WAV, FLAC: all the audio file formats explained," Published July 24, 2022, What Hi Fi. [Online]. Available: https://www.whathifi.com/advice/mp3-aac-wav-flac-all-the-audio-file-formats-explained.

