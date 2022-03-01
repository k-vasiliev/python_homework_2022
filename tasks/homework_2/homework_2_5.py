CURRENT_YEAR = 2022

student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)

"""
Формат данных - ('имя', год рождения, [оценки])
Выполните пункты ниже, используя переменную student
"""
# выведите фамилию и имя Ивана в формате "Студент: {Фамилия}, {Имя}"
student_full_name = student[0].split()
student_full_name.reverse()
print('Студент:', tuple(student_full_name))
# Выведите возраст Ивана в формате "Возраст: {возраст}".
student_age = CURRENT_YEAR - student[1]
print('Возраст:', student_age)
# Для определения текущего года используйте переменную CURRENT_YEAR

# напечатайте оценки Ивана через запятую в формате "Оценки: {оценка1}, {оценка2}"
student_grade = student[2]
print(f"Оценки:", {student_grade[0]}, {student_grade[1]}, {student_grade[2]}, {student_grade[3]}, {student_grade[4]})
# напечатайте средний балл Ивана в формате "Средний бал: {бал}"
# Сумму элементов списка можно найти с помощью функции sum()
sum_grades = sum(student_grade)
num_grades = len(student_grade)
avr_grade = sum_grades/num_grades

print('Средний бал:', avr_grade)
# Если средняя оценка Ивана больше или равна 8, то он получает повышенную стипендию.
# Выведите "Повышенная стипендия: есть/нет" в зависимости от его оценок
if avr_grade >= 8:
    print('Повышенная стипендия:', 'есть')
else:
    print('Повышенная стипендия:', 'нет')
