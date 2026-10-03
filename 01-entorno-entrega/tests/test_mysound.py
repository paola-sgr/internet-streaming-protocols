import unittest
from mysound import Sound


class TestSound(unittest.TestCase):

    def test_values(self):
        sound = Sound(2)
        sound.sin(440, 10000)

        # Check that sin wave values are within expected range
        self.assertTrue(all(-Sound.max_amplitude <= x <= Sound.max_amplitude
                            for x in sound.buffer))
        # Check specific sample values which should be 0
        self.assertEqual(0, sound.buffer[0])
        self.assertEqual(0, sound.buffer[22050])
        self.assertEqual(0, sound.buffer[44100])

        # Check specific sample values which should be maximum
        # Maximum amplitude in Pi/4 samples (i + 0.25 periods)
        period = 44100 / 440
        self.assertAlmostEqual(10000, sound.buffer[int(period * 0.25)],
                               delta=2)
        self.assertAlmostEqual(10000, sound.buffer[int((period) * 1.25)],
                               delta=2)

    def test_nsamples(self):
        sound = Sound(1)
        self.assertTrue(44100, len(sound.buffer))
        self.assertTrue(44100, sound.nsamples)

        sound = Sound(2)
        self.assertTrue(44100 * 2, len(sound.buffer))
        self.assertTrue(44100 * 2, sound.nsamples)


class TestBars(unittest.TestCase):

    def test_bars(self):
        sound = Sound(0.01)
        sound.sin(440, 10000)

        bars = sound.bars(bar_period=0.0001) # bar_period define la resolucion temporal de cada barra

        # Check number of lines
        self.assertAlmostEqual(112, len(bars.split('\n')), delta=1)

        # Check bar length
        self.assertAlmostEqual(41, len(bars.split('\n')[0]), delta=1)

        # Check positive bar
        self.assertEqual(' ' * 40 + ':', bars.split('\n')[0])
        self.assertEqual(' ' * 40 + ':' + '*' * 12, bars.split('\n')[1])
        self.assertEqual(' ' * 40 + ':' + '*' * 20, bars.split('\n')[2])
        self.assertEqual(' ' * 40 + ':' + '*' * 28, bars.split('\n')[3])
        self.assertEqual(' ' * 40 + ':' + '*' * 32, bars.split('\n')[4])
        self.assertEqual(' ' * 40 + ':' + '*' * 36, bars.split('\n')[5])

        # Check negative bar
        self.assertEqual(' ' * 33, bars.split('\n')[9][:33])


if __name__ == '__main__':
    unittest.main()
