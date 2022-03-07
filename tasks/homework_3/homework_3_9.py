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

user_input_str_list = user_input.split()

user_input_int_list = list(map(lambda x: int(x), user_input_str_list))

max_number = user_input_int_list[0]
min_number = user_input_int_list[0]

for i in user_input_int_list:
    if i > max_number:
        max_number = i
    elif i < min_number:
        min_number = i

print('Наибольшее число:', max_number)
print('Наименьшее число:', min_number)