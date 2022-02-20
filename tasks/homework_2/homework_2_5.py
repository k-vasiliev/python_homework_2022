CURRENT_YEAR = 2022

student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)

"""
Формат данных - ('имя', год рождения, [оценки])
Выполните пункты ниже, используя переменную student
"""

# выведите фамилию и имя Ивана в формате "Студент: {Фамилия}, {Имя}"

# Выведите возраст Ивана в формате "Возраст: {возраст}".
# Для определения текущего года используйте переменную CURRENT_YEAR

# напечатайте оценки Ивана через запятую в формате "Оценки: {оценка1}, {оценка2}"

# напечатайте средний балл Ивана в формате "Средний бал: {бал}"
# Сумму элементов списка можно найти с помощью функции sum()

# Если средняя оценка Ивана больше или равна 8, то он получает повышенную стипендию.
# Выведите "Повышенная стипендия: есть/нет" в зависимости от его оценок


# Решение

name_surname = student[0].replace(' ', ',')
find_space = student[0].find(' ')
surname = name_surname[find_space+1:]
name = name_surname[0:find_space]
name_surname = surname+', '+name
age = CURRENT_YEAR - student[1]
estimates = student[2]
estimates_to_string = ', '.join([str(x) for x in estimates])
avg_estimates = sum(estimates) / len(estimates)
if avg_estimates >= 8:
    result = 'есть'
else:
    result = 'нет'

print(f'Студент: {name_surname}\nВозраст: {age}\nОценки: {estimates_to_string}\nСредний бал: {avg_estimates}\n'
      f'Повышенная стипендия: {result}')
