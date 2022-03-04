"""

Пользователь вводит число
Посчитайте общее количество цифр и уникальных. Выведите через запятую без пробела

Вход: 922383
Выход: 6,4

"""

number = int(input())

str_number = str(number)
set_number = set(str_number)

print(len(str_number), end=",")
print(len(set_number))
