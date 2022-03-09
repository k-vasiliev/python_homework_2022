"""

Пользователь вводит строку, состоящую из чисел, разделенных пробелом
Используя циклы, найдите наибольшее и наименьшее число в этом списке

Не используйте стандартные функции min и max!

Вход: 10 8 3 15
Выход:
Наибольшее число: 15
Наименьшее число: 3

"""

user_input = input()
values = user_input.split()
max_values = float("-inf")
min_values = float("inf")
for i in values:
    if int(i) > max_values:
        max_values = int(i)
    elif int(i) <= min_values:
        min_values = int(i)
print(f'Наибольшее число:', max_values)
print(f'Наименьшее число:', min_values)