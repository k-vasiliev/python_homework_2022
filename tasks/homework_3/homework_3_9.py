"""

Пользователь вводит строку, состоящую из чисел, разделенных пробелом
Используя циклы, найдите наибольшее и наименьшее число в этом списке

Не используйте стандартные функции min и max!

Вход: 10 8 3 15
Выход:
Наибольшее число: 15
Наименьшее число: 3

"""

user_input = list(map(int, input().split()))

max_value = user_input[0]

for z in user_input:
    if z > max_value:
        print(z)

min_value = user_input[0]
for y in user_input:
    if y < min_value:
        min_value = y

print(min_value)
