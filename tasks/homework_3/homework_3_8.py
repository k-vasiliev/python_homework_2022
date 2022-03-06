"""
Пользователь вводит число
Посчитайте общее количество цифр и уникальных. Выведите через запятую без пробела
Вход: 922383
Выход: 6,4
"""
number = int(input('Ввести число: '))
list = list(str(number))
unigue = set(str(number))
print(f'{len(list)}, {len(unigue)}')
