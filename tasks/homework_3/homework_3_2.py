"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"
Выход:
Цифры: 3
Буквы: 5

"""

user_input = input("Введите набор букв и цифр: ")
print("Цифры:", len([i for i in user_input if i.isdigit()]))
print("Буквы:", len([i for i in user_input if i.isalpha()]))


