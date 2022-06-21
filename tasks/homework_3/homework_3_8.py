"""

Пользователь вводит число
Посчитайте общее количество цифр и уникальных. Выведите через запятую без пробела

Вход: 922383
Выход: 6,4

"""
count = 0
number = input()
number = list(map(int, number))
print(f"{len(number)},{len(set(number))}")




