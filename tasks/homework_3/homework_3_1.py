"""
Пользователь вводит строку с клавиатуры
Найти частоту слов в строке

Вход: "Я не кидал никого никогда"

Выход:

Я:1
не:1
кидал:1
никого:1
никогда:1

"""

user_input = input()

user_input_list = user_input.lower().split()
frequency = {}

for i in user_input_list:
    frequency.update({i: user_input_list.count(i)})

for key, value in frequency.items():
    print(key, value, sep=':')

