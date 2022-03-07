"""

Пользователь вводит число
Посчитайте общее количество цифр и уникальных. Выведите через запятую без пробела

Вход: 922383
Выход: 6,4

"""

number = int(input())

numbers_list = []

while number > 0:
    digit = number % 10
    number //= 10
    numbers_list.append(digit)

numbers_set = set(numbers_list)

print(len(numbers_list), len(numbers_set), sep=',')
