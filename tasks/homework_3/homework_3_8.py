"""

Пользователь вводит число
Посчитайте общее количество цифр и уникальных. Выведите через запятую без пробела

Вход: 922383
Выход: 6,4

"""

number = int(input())
number_string = str(number)
digit_list = list(number_string)
digit_set = set(digit_list)
print(f"{len(number_string)},{len(digit_set)}")
