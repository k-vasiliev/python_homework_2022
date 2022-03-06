"""
Пользователь вводит строку, состоящую из чисел, разделенных пробелом
Используя циклы, найдите наибольшее и наименьшее число в этом списке
Не используйте стандартные функции min и max!
Вход: 10 8 3 15
Выход:
Наибольшее число: 15
Наименьшее число: 3
"""
user_input = input('Ввести числа: ')
list = user_input.split()
min = int(list[0])
max = int(list[0])
for number in list:
    if int(number) < min:
        min = int(number)
    if int(number) > max:
        max = int(number)
print('Наибольшее число:', max)
print('Наименьшее число:', min)
