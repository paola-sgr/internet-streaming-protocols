import unittest
from mysoundsin import SoundSin
from mysound import Sound


class TestSoundSin(unittest.TestCase):

    def test_init_creates_buffer(self):
        # Comprobar que SoundSin inicializa el buffer correctamente
        sound = SoundSin(1, 440, 10000)
        self.assertEqual(len(sound.buffer), sound.nsamples)
        self.assertEqual(len(sound.buffer), 44100) # Para 1 segundo -> 44100 muestras

    def test_equivalence_with_sound(self):
        # Comprobar que SoundSin genera el mismo buffer que Sound+sin()
        s1 = Sound(1)
        s1.sin(440, 10000)

        s2 = SoundSin(1, 440, 10000)

        self.assertEqual(s1.buffer, s2.buffer)

    def test_inherited_bars_function(self):
        # Comprobar que la función heredada bars() funciona en SoundSin
        sound = SoundSin(0.01, 440, 10000)
        bars_output = sound.bars(bar_period=0.0001)

        # Debe generar un string multilínea
        self.assertIsInstance(bars_output, str)
        self.assertGreater(len(bars_output.split('\n')), 5) # Exige que haya más de 5 líneas


if __name__ == "__main__":
    unittest.main()
