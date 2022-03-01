CURRENT_YEAR = 2022

student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)

"""
Формат данных - ('имя', год рождения, [оценки])
Выполните пункты ниже, используя переменную student
"""

# выведите фамилию и имя Ивана в формате "Студент: {Фамилия}, {Имя}"
print(f"Студент: {student[0]}")
# Выведите возраст Ивана в формате "Возраст: {возраст}".
age = CURRENT_YEAR - int(student[1])
print(f"Возраст: {age}")
# Для определения текущего года используйте переменную CURRENT_YEAR

# напечатайте оценки Ивана через запятую в формате "Оценки: {оценка1}, {оценка2}"
print(f"Оценки: {student[2][0]}, {student[2][1]}")
# напечатайте средний балл Ивана в формате "Средний балл: {балл}"
# Сумму элементов списка можно найти с помощью функции sum()
sum_grade = sum(student[2])
average_grade = sum_grade / len(student[2])
# Если средняя оценка Ивана больше или равна 8, то он получает повышенную стипендию.
# Выведите "Повышенная стипендия: есть/нет" в зависимости от его оценок
if average_grade >= 8:
     print("Повышенная стипендия: есть")
else:
     print("Повышенная стипендия: нет")

