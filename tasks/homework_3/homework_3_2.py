"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"

Выход:

Цифры: 3
Буквы: 5

"""
user_input = input()
user_123 = 0
user_abc = 0
for c in user_input:
    if c.isdigit():
        user_123 += 1
    else:
        if c.isalpha():
            user_abc += 1

print('Цифры: ', user_123)
print('Буквы: ', user_abc)
