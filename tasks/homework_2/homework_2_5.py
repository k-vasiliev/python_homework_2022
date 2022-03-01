CURRENT_YEAR = 2022

student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)

"""
Формат данных - ('имя', год рождения, [оценки])
Выполните пункты ниже, используя переменную student
"""

# выведите фамилию и имя Ивана в формате "Студент: {Фамилия}, {Имя}"
fullname = student[0]
a = fullname.find(' ')
name = fullname[:a]
familyname = fullname[a+1:]
print(f"Студент: {familyname}, {name}")

# Выведите возраст Ивана в формате "Возраст: {возраст}".
# Для определения текущего года используйте переменную CURRENT_YEAR
birthyear = student[1]
from datetime import datetime
current_year = datetime.now().year
age = current_year - birthyear
print(f"Возраст: {age}")

# напечатайте оценки Ивана через запятую в формате "Оценки: {оценка1}, {оценка2}"
marks = list(student[2])
mark0 = marks[0]
mark1 = marks[1]
mark2 = marks[2]
mark3 = marks[3]
mark4 = marks[4]
print(f"Оценки: {mark0}, {mark1}, {mark2}, {mark3}, {mark4}")

# напечатайте средний балл Ивана в формате "Средний бал: {бал}"
# Сумму элементов списка можно найти с помощью функции sum()
avg = sum(marks)/len(marks)
print(f"Средний бал: {avg}")

# Если средняя оценка Ивана больше или равна 8, то он получает повышенную стипендию.
# Выведите "Повышенная стипендия: есть/нет" в зависимости от его оценок
if avg >= 8:
    print(f"Повышенная стипендия: есть")
else:
    print(f"Повышенная стипендия: нет")