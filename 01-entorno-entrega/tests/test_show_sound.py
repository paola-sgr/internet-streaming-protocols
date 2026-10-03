import contextlib
import io
import os
import subprocess
import unittest

import show_sound

this_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(this_dir, '..')


class TestShow(unittest.TestCase):

    def test_main(self):
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            os.chdir(parent_dir)
            show_sound.main(0.01, 880, 0.0001)
        output = stdout.getvalue()

        # Check output has correct number of lines
        self.assertEqual(113, len(output.split('\n')))

    def test_args(self):
        command = subprocess.run(['python3', 'show_sound.py',
                                  '0.01', '880', '0.0001'],
                                 cwd=parent_dir, text=True,
                                 stdout=subprocess.PIPE,
                                 stderr=subprocess.STDOUT)
        output = command.stdout
        self.assertEqual(113, len(output.split('\n')))


if __name__ == '__main__':
    unittest.main()
