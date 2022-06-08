"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"

Выход:

Цифры: 3
Буквы: 5

"""

user_input = input()
new_input = user_input.replace(" ", "")

summa_digits = 0
summa_chars = 0

for i in new_input:
    if i.isdigit():
        summa_digits += 1
    else:
        summa_chars += 1
print(f' Цифры: {summa_digits}\n Буквы: {summa_chars}')
