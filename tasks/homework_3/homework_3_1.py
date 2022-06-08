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
user_input_list = user_input

distinct_user_input_list = list()
for i in user_input_list:
    if distinct_user_input_list.count(i) == 0:
        distinct_user_input_list.append(i)
        word_count = user_input_list.count(i)
        print(f'{i}: {word_count}')
    else:
        continue
