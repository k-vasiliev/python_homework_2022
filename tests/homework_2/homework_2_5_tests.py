import io
import unittest
from contextlib import redirect_stdout


class HomeworkTest(unittest.TestCase):

    def test_homework_2_5(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            import tasks.homework_2.homework_2_5
            output = buf.getvalue().split("\n")
            self.assertEqual("Студент: Питонов, Иван", output[0], "Неправильный вывод имени и фамилии")
            self.assertEqual("Возраст: 21", output[1], "Неправильный вывод возраста")
            self.assertEqual("Оценки: 8, 7, 7, 9, 6", output[2], "Неправильный вывод оценок")
            self.assertEqual("Средний бал: 7.4", output[3], "Неправильный вывод среднего балла")
            self.assertEqual("Повышенная стипендия: нет", output[4], "Неправильный вывод информации о стипенди")


if __name__ == '__main__':
    unittest.main()
