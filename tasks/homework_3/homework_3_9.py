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
max = user_inp_list[0]
min = user_inp_list[0]
for x in user_inp_list:
   if x > max:
       max = x
for x in user_inp_list:
    if x < min:
        min = x
print('Наибольшее число:', max)
print('Наименьшее число:', min)
