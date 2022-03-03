"""

Пользователь вводит число
Посчитайте общее количество цифр и уникальных. Выведите через запятую без пробела

Вход: 922383
Выход: 6,4

"""

number = int(input())
number_list = list(str(number))
number_set = set(str(number))

print(f'{len(number_list)},{len(number_set)}')
