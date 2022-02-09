import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class HomeworkTest(unittest.TestCase):

    fake_input_1 = iter(['Hello, world', "Hello"]).__next__

    @patch('builtins.input', fake_input_1)
    def test_homework(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            import tasks.homework_2.homework_2_2
            output = buf.getvalue().split("\n")
            self.assertEqual(", world", output[0], "Неправильный вывод")

if __name__ == '__main__':
    unittest.main()
