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
user_input_list = user_input.split()

distinct_user_input_list = list()

for word in user_input_list:
    if distinct_user_input_list.count(word) == 0:
        distinct_user_input_list.append(word)
        word_count = user_input_list.count(word)
        print(f'{word}: {word_count}')
