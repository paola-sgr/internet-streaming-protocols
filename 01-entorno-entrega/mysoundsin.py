#! /usr/bin/env python3

import mysound


class SoundSin(mysound.Sound):
    def __init__(self, duration, frequency, amplitude):
        # Inicializamos como un Sound normal
        super().__init__(duration)

        # Generamos ya la onda sinusoidal al crear el objeto
        self.sin(frequency, amplitude)


# sonido = SoundSin(0.01, 440, 10000)
# print(sonido.bars(0.001))
