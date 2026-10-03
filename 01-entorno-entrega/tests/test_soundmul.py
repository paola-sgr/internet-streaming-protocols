import unittest
from mysound import Sound


class TestSoundMul(unittest.TestCase):

    def test_multiply_by_one(self):
        # Multiplicar por 1 debe dejar el buffer igual
        s = Sound(0.01)
        s.sin(440, 10000)

        s2 = s.soundmul(1.0)

        self.assertEqual(s.buffer, s2.buffer)
        self.assertEqual(len(s.buffer), len(s2.buffer))

    def test_multiply_by_zero(self):
        # Multiplicar por 0 debe dar un buffer de ceros
        s = Sound(0.01)
        s.sin(440, 10000)

        s2 = s.soundmul(0.0)

        self.assertTrue(all(x == 0 for x in s2.buffer))
        self.assertEqual(len(s.buffer), len(s2.buffer))

    def test_multiply_with_factor(self):
        # Multiplicar por un factor distinto escala los valores
        s = Sound(0.01)
        s.sin(440, 10000)

        s2 = s.soundmul(0.5)

        # Cada valor del buffer debe ser aproximadamente la mitad
        # recorriendo los índices
        for i in range(len(s.buffer)):
            self.assertAlmostEqual(s2.buffer[i], int(s.buffer[i] * 0.5), delta=1)



if __name__ == '__main__':
    unittest.main()
