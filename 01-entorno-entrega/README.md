# 01 - Python y entorno de desarrollo

Primera práctica de la asignatura *Protocolos para la Transmisión de Audio y Vídeo en Internet* (PTAVI), del grado en Ingeniería de Sistemas Audiovisuales y Multimedia.

El objetivo es repasar la programación orientada a objetos en Python y el flujo de trabajo con git que se usa durante el resto del curso: partiendo de una clase que representa un sonido digital, se amplía con herencia, se prueba con tests automáticos y se ajusta a la guía de estilo PEP 8.

## Qué contiene

*Archivo: Descripción:*
- `mysound.py`: Clase `Sound`, que guarda muestras de sonido como una lista de enteros. Aquí añadí el método `soundmul`.
- `show_sound.py`: Programa que muestra un sonido por pantalla (proporcionado en la plantilla).
- `mysoundsin.py`: Clase `SoundSin`, que hereda de `Sound` y crea directamente una señal sinusoidal.
- `tests/`: Pruebas con `unittest` de las clases anteriores.

## Lo que implementé

- Estudiar la clase `Sound` (muestras de audio como lista de enteros) y escribir pruebas con `unittest`.
- Crear la clase `SoundSin`, que hereda de `Sound` y genera directamente una señal sinusoidal.
- Añadir el método `soundmul`, que devuelve un sonido nuevo con las muestras multiplicadas por un factor.
- Escribir tests para cada parte.
- Ajustar el código a la guía de estilo PEP 8.

## Tecnologías

Python 3 · unittest · pycodestyle · git

## Cómo ejecutarlo

Requiere Python 3. Desde esta carpeta:

```bash
# Ejecutar todos los tests
python3 -m unittest discover -s tests

# Comprobar el estilo PEP 8
pycodestyle *.py tests/*.py
```
