import io
import unittest
from contextlib import redirect_stdout

from tasks import homework_1


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            homework_1.print_student_info(('Иван Питонов', 2001, [8, 7, 7, 9, 6], True))
            output = buf.getvalue().split("\n")
            self.assertEqual("Студент: Питонов, Иван", output[0])
            self.assertEqual("Возраст: 21", output[1])
            self.assertEqual("Оценки: 8, 7, 7, 9, 6", output[2])
            self.assertEqual("Средний бал: 7.4", output[3])
            self.assertEqual("Повышенная стипендия: нет", output[4])


if __name__ == '__main__':
    unittest.main()
