# Taller_Instrumentacion

## 4. ¿Qué es ruido de cuantización? ¿Bajo que circunstancias se podría modelar como ruido aditivo?

El ruido de cuantización es un tipo de error que se introduce cuando se convierte una señal analógica en una señal digital. Esto sucede porque la señal digital solo puede tener valores discretos, mientras que la señal analógica puede tener valores continuos [1]. 
Un ejemplo en el que el ruido de cuantización puede ser modelado como ruido aditivo es cuando se cuantifica una señal sinusoidal. En este caso, la relación señal-ruido de cuantización (SQNR) se puede calcular como la relación entre la potencia promedio de la señal y la potencia promedio del ruido de cuantización

## 5. ¿Para una grabación de audio, el piso de ruido de la señal es predominado por el ruido de cuantización o el ruido térmico?

n una grabación de audio, el piso de ruido de la señal puede ser afectado tanto por el ruido de cuantización como por el ruido térmico.

## 6. ¿Cuales son las tasas de muestreo más populares para grabaciones de audio? ¿La cantidad de bits por muestra?

Las tasas de muestreo más comunes para grabaciones de audio son 44.1 kHz y 48 kHz. También hay tasas de muestreo más altas disponibles, como 88.2 kHz, 96 kHz y 192 kHz. En cuanto a la cantidad de bits por muestra son de 16 bits y 24 bits.


## 7. ¿Cuales son los formatos de audio cuya compresión o almacenamiento no agrega distorsión?
Cuando se trata de analizar los efectos de la compresión con pérdidas uno de estos es la distorsión, sin embargo si se quiere mantener la integridad de la señal original sin ningún tipo de pérdidas se pueden hacer uso de los formatos de compresión sin pérdidas con la única desventaja de tender a ser archivos de mayor tamaño. Los formatos sin pérdidas en la actualidad son:[2]
1. ALAC: desarrollado por Apple con una resolución entre 16-bit/44.1 kHz (calidad de un disco) y 24-bit/192 kHz. Es importante notar que a pesar de que se use ese algoritmo de codificación la extensión de los archivos no es .alac en cambio podría parecer ser de formatos con pérdidas como .m4a no obstante estos son usados solo como contenedores pero el archivo sin pérdidas se encuentran dentro.
2. FLAC: este formato de compresión sin pérdida admite frecuencias de muestreo de alta resolución, ocupa aproximadamente la mitad del espacio de un archivo WAV y almacena metadatos. Este es de fuente libre por lo que es gratis, además, se considera el formato preferido para descargar y almacenar álbumes de alta resolución.
3. MQA: es un formato que utiliza técnicas con y sin pérdidas, sin embargo, este es considerado audiblemente sin pérdidas. Por medio de esta técnica genera archivos de menor tamaño por lo que es óptimo para plataformas de "streaming" o transmisión.
4. WMA lossless: es un formato sin pérdidas propuesto para "Windows Media Audio", sin embargo, en la actualidad ya no es utilizado y mucho teléfonos no son compatibles con susodicho.
## 8. ¿Cómo se puede utilizar un barrido de frecuencias para modelar la respuesta en frecuencia de un dispositivo bajo prueba (DUT)? Investigue el procedimiento a realizar a cada grabación de audio para tener la estimación de la respuesta en frecuencia.
Para modelar la respuesta en frecuencia de un DUT se pueden seguir los siguientes pasos:
1. Generación del audio: es necesario generar un archivo de audio que realice el barrrido de 50Hz hasta 5kHz.
2. Configuración del equipo: para esto se debe disponer del archivo antes generado y se debe preparar tanto un micrófono como un parlante ecualizado para poder realizar la medición. El micrófono debe estar configurado para una codificación sin pérdidas.
3. Medición: para la medición el micrófono y el parlante debe estar a una distancia corta medida y se debe empezar a grabar apenas empieza el parlante a emitir la señal.
4. Análisis de grabaciones: una vez se obtenga el audio grabado, este debe ser transferido a la computadora para ser procesado, el cual debe ser expuesto a una ventana de Hamming y luego a una transformada de Fourier rápida así se obtendría el espectro en frecuencia de dicha señal.
5. Presentación de resultados: a partir de los datos obtenidos después del proceso de la transformada de Fourier se pueden graficar de forma semilogarítmica por medio de alguna biblioteca en python como matplotlib.



Referencias:
[1] B. Widrow & I. Kollár , "Quantization Noise: Roundoff Error in Digital Computation, Signal Processing, Control, and Communications," Published 2008, Cambridge University Press. 

[2] B. Scarrott, "MP3, AAC, WAV, FLAC: all the audio file formats explained," Published July 24, 2022, What Hi Fi. [Online]. Available: https://www.whathifi.com/advice/mp3-aac-wav-flac-all-the-audio-file-formats-explained.

