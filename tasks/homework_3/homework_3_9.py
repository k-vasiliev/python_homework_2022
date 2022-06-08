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
user_input_list = (user_input).split(' ')

maXX = int(user_input_list[0])
miNN = int(user_input_list[0])

for i in user_input_list:
    if int(i) > maXX:
        maXX = int(i)
    if int(i) < miNN:
        miNN = int(i)


print(f'Наибольшее число: {maXX}\nНаименьшее чесло: {miNN}')