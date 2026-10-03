import unittest

from mysound import Sound

class TestBar(unittest.TestCase):

    def test_positive_bar(self):
        # Un valor positivo debe generar una barra con ':' después de los espacios
        bar = Sound._bar(5000)
        self.assertTrue(bar.startswith(' ' * 40 + ':'))
        self.assertIn('*', bar) # Debe contener estrellas

    def test_negative_bar(self):
        # Un valor negativo debe generar una barra con ':' al final
        bar = Sound._bar(-5000)
        self.assertTrue(bar.endswith(':'))
        self.assertIn('*', bar)
        self.assertEqual(bar.index(':'), len(bar) - 1) # ':' debe estar al final

if __name__ == '__main__':
    unittest.main()
