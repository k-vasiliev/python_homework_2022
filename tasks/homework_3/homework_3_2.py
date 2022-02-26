"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"

Выход:

Цифры: 3
Буквы: 5

"""

user_input = input()
counter_num = 0
counter_alpha = 0

for i in user_input:
    if i.isnumeric():
        counter_num += 1
    if i.isalpha():
        counter_alpha += 1

print(f'Цифры: {counter_num}\nБуквы: {counter_alpha}')
