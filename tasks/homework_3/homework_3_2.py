"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"
Выход:
Цифры: 3
Буквы: 5
"""
user_input = input('Ввести строку с клавиатуры: ')
some_number = 0
some_letter = 0
for x in user_input:
    some_number += x.isnumeric()
    some_letter += x.isalpha()
print(f"Цифры: {some_number}")
print(f"Буквы: {some_letter}")