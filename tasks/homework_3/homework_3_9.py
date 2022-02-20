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

# разделяем по пробелу и преобразуем в числа
input_tuple = tuple(map(int, user_input.split(' ')))

# ищем min и max
max_value = input_tuple[0]
min_value = input_tuple[0]
for element in input_tuple:
    if max_value < element:
        max_value = element
    if min_value > element:
        min_value = element

print(f"Наибольшее число: {max_value}")
print(f"Наименьшее число: {min_value}")
