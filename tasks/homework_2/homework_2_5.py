student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)
"""
Формат данных - ('имя', год рождения, [оценки])
Выполните пункты ниже, используя переменную student
"""
# выведите фамилию и имя Ивана в формате "Студент: {Фамилия}, {Имя}"
surname = 'Питонов'
name = 'Иван'
surname_name = (surname + ', '+name)
print(f'Студент: {surname_name}')
# Выведите возраст Ивана в формате "Возраст: {возраст}".
# Для определения текущего года используйте переменную CURRENT_YEAR
CURRENT_YEAR = 2022
age = CURRENT_YEAR - student[1]
print(f'Возраст: {age}')
# напечатайте оценки Ивана через запятую в формате "Оценки: {оценка1}, {оценка2}"
grade = student[2]
print(f'Оценки: {(grade[0])}, {(grade[1])}, {(grade[2])}, {(grade[3])}, {(grade[4])}', sep = ', ')
# напечатайте средний балл Ивана в формате "Средний бал: {бал}"
# Сумму элементов списка можно найти с помощью функции sum()
grade = student[2]
sum_grade = sum(grade)
number_of_values = len(grade)
average = sum_grade / number_of_values
print(f'Средний бал: {average}')
# Если средняя оценка Ивана больше или равна 8, то он получает повышенную стипендию.
# Выведите "Повышенная стипендия: есть/нет" в зависимости от его оценок
grade = student[2]
sum_grade = sum(grade)
number_of_values = len(grade)
average = sum_grade / number_of_values
if average >= 8:
    print('Повышенная стипендия: есть')
else:
    print('Повышенная стипендия: нет')
