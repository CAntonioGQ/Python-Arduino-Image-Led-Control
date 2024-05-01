# Control de LEDs mediante detección de colores con Python y Arduino

Este proyecto ofrece una manera divertida de interactuar con LEDs mediante la detección de colores en tiempo real utilizando Python y Arduino. La detección de colores se realiza mediante visión por computadora con OpenCV, y los comandos para controlar los LEDs se envían a través de comunicación serial a una placa Arduino.

## Requisitos

- Python 3.x
- OpenCV (cv2)
- Numpy
- Pyserial
- Arduino IDE
- Placa Arduino
- LEDs y resistencias

## Configuración

1. Conecta los LEDs a los pines correspondientes de la placa Arduino según se especifica en el código.
2. Carga el sketch de Arduino en la placa.
3. Asegúrate de tener las bibliotecas necesarias instaladas en tu entorno de Python.
4. Verifica el puerto serial utilizado por Arduino y actualiza el código de Python si es necesario.

## Uso

1. Ejecuta el script de Python `pythonColorDetection.py`.
2. La cámara se abrirá y comenzará a detectar los colores rojo y verde en tiempo real.
3. Cuando se detecte el color rojo, el LED verde se encenderá y el LED rojo se apagará.
4. Cuando se detecte el color verde, el LED rojo se encenderá y el LED verde se apagará.
5. Cuando no se detecte ningún color, ambos LEDs permanecerán apagados.
6. Presiona 'q' para salir del programa.

## Personalización

- Ajusta los rangos de color en el código de Python para detectar diferentes tonos de rojo y verde según tus necesidades.
- Modifica los pines de los LEDs en el código de Arduino si utilizas diferentes pines.
- Agrega más colores y LEDs siguiendo la misma lógica en ambos códigos.

## Contribución

¡Las contribuciones son bienvenidas! Si tienes alguna mejora o nueva característica, no dudes en enviar un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
