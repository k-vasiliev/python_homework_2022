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
user_inp_list = user_input.split(' ')
user_inp_list = [int(n) for n in user_inp_list]
max_ = user_inp_list[0]
min_ = user_inp_list[0]
for x in user_inp_list:
   if x > max_:
       max_ = x
for x in user_inp_list:
    if x < min_:
        min_ = x
print('Наибольшее число:', max_)
print('Наименьшее число:', min_)
