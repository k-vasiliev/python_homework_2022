"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"

Выход:

Цифры: 3
Буквы: 5

"""

user_input = input()
digits_counter = 0
letter_counter = 0

for ch in user_input:
    # если это цифра, то увеличиваем счётчик
    if ch.isdigit():
        digits_counter += 1
    elif ch != " ":
        # если не цифра и не пробел, то буква
        letter_counter += 1

print(f"Цифры: {digits_counter}")
print(f"Буквы: {letter_counter}")
