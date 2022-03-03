"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"

Выход:

Цифры: 3
Буквы: 5

"""

user_input = input()

symbols = [s for s in user_input.replace(' ', '')]

numbers = 0
letters = 0

for x in symbols:
    if x.isnumeric():
        numbers += 1
    else:
        letters += 1

print(numbers)
print(letters)
