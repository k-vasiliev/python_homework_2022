"""

Пользователь вводит число
Посчитайте общее количество цифр и уникальных. Выведите через запятую без пробела

Вход: 922383
Выход: 6,4

"""

number = int(input())

number_sum = len(str(number))

number1 = []

count = 0

for i in str(number):
    if i not in number1:
        count += 1
        number1.append(i)

print(number_sum, ",", count)


