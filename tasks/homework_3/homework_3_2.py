"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"

Выход:

Цифры: 3
Буквы: 5

"""

user_input = input()
count1 = 0
count2 = 0
for i in user_input:
    if i.isdigit() is True:
        count1 += 1
    if i.isalpha() is True:
        count2 += 1

print(f"Цифры: {count1}")
print(f"Буквы: {count2}")
