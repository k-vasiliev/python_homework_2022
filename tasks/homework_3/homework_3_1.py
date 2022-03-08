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

words_dict = {}

for i in user_input.split():
    words_dict[i] = words_dict.get(i, 0) + 1

for key in words_dict:
    print("{} : {}".format(key, words_dict[key]))
