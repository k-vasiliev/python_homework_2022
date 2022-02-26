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

user_input = input().split()
for i in range(len(user_input)):
    print(f'{user_input[i]}:{user_input.count(user_input[i])}')
