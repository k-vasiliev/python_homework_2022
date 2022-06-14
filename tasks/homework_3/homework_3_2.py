"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"

Выход:

Цифры: 3
Буквы: 5

"""

user_input = input()

dict = {'Цифры': 0, 'Буквы': 0, 'Спец.символы': 0}
for i in user_input:
    if i.isdigit():
        dict['Цифры'] += 1
    elif i.isalpha():
        dict['Буквы'] += 1
    else:
        dict['Спец.символы'] += 1

for key,value in dict.items():
    print(key, ':', value)
