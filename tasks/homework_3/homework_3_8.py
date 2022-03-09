"""

Пользователь вводит число
Посчитайте общее количество цифр и уникальных. Выведите через запятую без пробела

Вход: 922383
Выход: 6,4

"""

number = int(input())

count = list(str(number))
unique = set(str(count))
print(f'{len(count)},{len(unique)}')


