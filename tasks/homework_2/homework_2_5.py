CURRENT_YEAR = 2022

student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)

"""
Формат данных - ('имя', год рождения, [оценки])
Выполните пункты ниже, используя переменную student
"""
# выведите фамилию и имя Ивана в формате "Студент: {Фамилия}, {Имя}"
student_full_name = student[0]
# дробим Фамилию и Имя, чтобы можно было печатать по индексам
student_full_name = student_full_name.split(' ')
print(f'Студент: {student_full_name[1]}, {student_full_name[0]}')
# Выведите возраст Ивана в формате "Возраст: {возраст}".
# Для определения текущего года используйте переменную CURRENT_YEAR
student_age = CURRENT_YEAR - student[1]
print(f'Возраст: {student_age}')
# напечатайте оценки Ивана через запятую в формате "Оценки: {оценка1}, {оценка2}"
student_marks = student[2]
student_marks1 = student_marks[1]
student_marks2 = student_marks[2]
print(f'Оценки: {student_marks1}, {student_marks2}')
# напечатайте средний балл Ивана в формате "Средний бал: {бал}"
# Сумму элементов списка можно найти с помощью функции sum()
average_marks = sum(student_marks)/len(student_marks)
print(f"Средний бал: {average_marks}")
# Если средняя оценка Ивана больше или равна 8, то он получает повышенную стипендию.
# Выведите "Повышенная стипендия: есть/нет" в зависимости от его оценок
if average_marks >= 8:
    print(f'Повышенная стипендия: есть')
else:
    print(f'Повышенная стипендия: нет')
