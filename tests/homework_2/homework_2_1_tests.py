import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class HomeworkTest(unittest.TestCase):

    @patch('builtins.input', return_value="teststring")
    def test_homework(self, input):
        with io.StringIO() as buf, redirect_stdout(buf):
            import tasks.homework_2.homework_2_1
            output = buf.getvalue().split("\n")
            self.assertEqual("10", output[0], "Неправильная длина слова")
            self.assertEqual("eststring", output[1], "Неправильное слово без первой буквы")
            self.assertEqual("g", output[2], "Неправильный последний символ")
            self.assertEqual("teststri", output[3], "Неправильное слово без двух последних букв")
            self.assertEqual("TESTSTRING", output[4], "Неправильное слово в uppercase")


if __name__ == '__main__':
    unittest.main()
