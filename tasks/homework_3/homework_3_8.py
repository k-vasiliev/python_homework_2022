"""

Пользователь вводит число
Посчитайте общее количество цифр и уникальных. Выведите через запятую без пробела

Вход: 922383
Выход: 6,4

"""

number = int(input())
number_list = list(str(number))
number_set = set(number_list)
unique = []
count = 0

for i in number_set:
    if i not in unique:
        count += 1
        unique.append(i)

print(f'{len(number_list)},{count}')
