"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"

Выход:

Цифры: 3
Буквы: 5

"""

user_input = input()
list_of_chars = list(user_input)

num_of_nums = 0
num_of_letters = 0
num_of_space = 0

for a in list_of_chars:
    if a.isnumeric() == True:
        num_of_nums += 1
    elif a == ' ':
        num_of_space += 1
    else:
        num_of_letters += 1

print(f'Цифры: {num_of_nums}')
print(f'Буквы: {num_of_letters}')
