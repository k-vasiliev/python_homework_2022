"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"

Выход:

Цифры: 3
Буквы: 5

"""

user_input = input()
user_input_list = list(user_input)

number_list = list()
letter_list = list()

for element in user_input_list:
    if element != ' ':
        if element.isnumeric() == True:
            number_list.append(element)
        else:
            letter_list.append(element)

print(f'Цифры: {len(number_list)}')
print(f'Буквы: {len(letter_list)}')
