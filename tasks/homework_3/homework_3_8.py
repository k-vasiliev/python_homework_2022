"""

Пользователь вводит число
Посчитайте общее количество цифр и уникальных. Выведите через запятую без пробела

Вход: 922383
Выход: 6,4

"""

number = int(input())

my_list = list()
my_set = set()

for i in str(number):
    my_list.append(i)
    my_set.add(i)

print(f'{len(my_list)}, {len(my_set)}')