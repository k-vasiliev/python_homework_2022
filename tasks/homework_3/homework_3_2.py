"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"

Выход:

Цифры: 3
Буквы: 5

"""

user_input = input()

user_input_list = list(user_input)

digits = []
letters = []

symbol_counter = 1

for i in user_input_list:
    if i.isnumeric() is True:
        digits.append(symbol_counter)
    elif i.isalpha() is True:
        letters.append(symbol_counter)

print('Цифры:', sum(digits))
print('Буквы:', sum(letters))
