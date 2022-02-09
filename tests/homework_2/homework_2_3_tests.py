import io
import sys
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

module_name = "tasks.homework_2.homework_2_3"

class HomeworkTest(unittest.TestCase):


    @patch('builtins.input', return_value="123")
    def test_is_numeric(self, input):
        with io.StringIO() as buf, redirect_stdout(buf):
            if module_name in sys.modules:
                del sys.modules["tasks.homework_2.homework_2_3"]

            import tasks.homework_2.homework_2_3
            output = buf.getvalue().split("\n")
            self.assertEqual("Это число!", output[0], "Неправильный вывод")

    @patch('builtins.input', return_value="1ф23")
    def test_is_not_numeric(self, input):
        with io.StringIO() as buf, redirect_stdout(buf):
            if module_name in sys.modules:
                del sys.modules["tasks.homework_2.homework_2_3"]

            import tasks.homework_2.homework_2_3
            output = buf.getvalue().split("\n")
            self.assertEqual("Это не число!", output[0], "Неправильный вывод")


if __name__ == '__main__':
    unittest.main()
