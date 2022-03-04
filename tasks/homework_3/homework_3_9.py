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

split_input = user_input.split(" ")
min_num = int(split_input[0])
max_num = int(split_input[0])

for x in range(len(split_input)):
    if min_num > int(split_input[x]):
        min_num = int(split_input[x])
    if max_num < int(split_input[x]):
        max_num = int(split_input[x])


print(f"Наибольшее число: {max_num}")
print(f"Наименьшее число: {min_num}")
