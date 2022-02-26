"""

Пользователь вводит число
Посчитайте общее количество цифр и уникальных. Выведите через запятую без пробела

Вход: 922383
Выход: 6,4

"""

number = int(input())
num_digits = len(str(number))
x = [x for x in str(number)]
to_int = list(map(int, x))
unique = len(set(to_int))
print(num_digits, unique, sep=',')
