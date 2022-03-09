"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"

Выход:

Цифры: 3
Буквы: 5

"""

user_input = input()
print(f"Цифры:", len([num for num in user_input if num.isdigit()]))
print(f"Буквы:", len([let for let in user_input if let.isalpha()]))
