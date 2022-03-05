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
list1 = list(user_input.split(' '))
list_enum = enumerate(list1)

for index, value in list_enum:
    if index == len(list1)-1:
        break
    next_value = list1[index+1]
    if value > next_value:
        print (f'{value}This bigger')

