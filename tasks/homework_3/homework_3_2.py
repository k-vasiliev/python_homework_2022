"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"

Выход:

Цифры: 3
Буквы: 5

"""

user_input = input()

numbers = list()
words = list()
for elem in user_input:
    if elem.isdigit():
        numbers.append(elem)
    else:
        if elem.isalpha():
            words.append(elem)
print('Цифры:', len(numbers))
print('Буквы:', len(words))

#2 вариант
print('Цифры:',len([i for i in user_input if i.isdigit()]))
print('Буквы:',len([i for i in user_input if i.isalpha()]))
