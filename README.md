# Taller_Instrumentacion

## 7. ¿Cuales son los formatos de audio cuya compresión o almacenamiento no agrega distorsión?
Cuando se trata de analizar los efectos de la compresión con pérdidas uno de estos es la distorsión, sin embargo si se quiere mantener la integridad de la señal original sin ningún tipo de pérdidas se pueden hacer uso de los formatos de compresión sin pérdidas con la única desventaja de tender a ser archivos de mayor tamaño. Los formatos sin pérdidas en la actualidad son:[1]
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
[1] https://www.whathifi.com/advice/mp3-aac-wav-flac-all-the-audio-file-formats-explained
