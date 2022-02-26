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
list_numbers = [int(x) for x in user_input.split()]
list_numbers2 = list_numbers.copy()
largest = 0
minimum = 0
for i in range(len(list_numbers) - 1):
    if list_numbers[i] > list_numbers[i + 1]:
        list_numbers[i + 1] = list_numbers[i]
    largest = list_numbers[i + 1]

if len(list_numbers) <= 1:
    largest = user_input[:]
else:
    largest = largest

print('Наибольшее число:', largest)

for i in range(len(list_numbers2) - 1):
    if list_numbers2[i] < list_numbers2[i + 1]:
        list_numbers2[i + 1] = list_numbers2[i]
    minimum = list_numbers2[i + 1]


if len(list_numbers2) <= 1:
    minimum = user_input[:]
else:
    minimum = minimum

print('Наименьшее число:', minimum)

"""
Уважаемые проверяющие, понимаю и осознаю, что очень костыльное решение, но уже и раньше сталкивалась с этой задачей 
и всегда брала за основу чужие алгоритмы, в этот раз решила придумать свой. Решение ниже тоже моё,но алгоритм известный
"""


# Решение 2
# user_input = input()
# list_numbers = [int(x) for x in user_input.split()]
# largest = None
# minimum = None
#
# for i in range(len(list_numbers)):
#     if largest is None or list_numbers[i] > largest:
#         largest = list_numbers[i]
#     if minimum is None or list_numbers[i] < minimum:
#         minimum = list_numbers[i]
# print('Наибольшее число:', largest)
# print('Наименьшее число:', minimum)
