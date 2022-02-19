CURRENT_YEAR = 2022

student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)

"""
Формат данных - ('имя', год рождения, [оценки])
Выполните пункты ниже, используя переменную student
"""

# выведите фамилию и имя Ивана в формате "Студент: {Фамилия}, {Имя}"
student_name_surname = student[0]
space_index = student_name_surname.find(' ')
student_name = student_name_surname[:space_index]
student_surname = student_name_surname[space_index+1:]
print('Студент:', student_surname, student_name)

# Выведите возраст Ивана в формате "Возраст: {возраст}".
# Для определения текущего года используйте переменную CURRENT_YEAR
age = CURRENT_YEAR - student[1]
print('Возраст:', age)

# напечатайте оценки Ивана через запятую в формате "Оценки: {оценка1}, {оценка2}"
marks = student[2]
print(f"Оценки: {marks[0]}, {marks[1]}, {marks[2]}, {marks[3]}, {marks[4]}")


# напечатайте средний балл Ивана в формате "Средний бал: {бал}"
# Сумму элементов списка можно найти с помощью функции sum()
average_mark = sum(marks)/len(marks)
print("Средний балл:", average_mark)

# Если средняя оценка Ивана больше или равна 8, то он получает повышенную стипендию.
# Выведите "Повышенная стипендия: есть/нет" в зависимости от его оценок
if average_mark >= 8:
    print('Повышенная стипендия: есть')
else:
    print('Повышенная стипендия: нет')
