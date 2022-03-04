"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"

Выход:

Цифры: 3
Буквы: 5

"""

user_input = input()
num = 0
letter = 0

for x in user_input:
    num += x.isnumeric()
    letter += x.isalpha()

print(f"Цифры: {num}")
print(f"Буквы: {letter}")
