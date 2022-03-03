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
user_input_list = user_input.split()
min_number = int(user_input_list[0])
max_number = int(user_input_list[0])

for number in user_input_list:
    if int(number) < min_number:
        min_number = int(number)
    if int(number) > max_number:
        max_number = int(number)

print('Наибольшее число:', max_number)
print('Наименьшее число:', min_number)
