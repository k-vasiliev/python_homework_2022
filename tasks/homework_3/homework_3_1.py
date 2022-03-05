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
list_of_words = list(user_input.rsplit(' '))
set_of_words = {}

for a in list_of_words:
    set_of_words[a] = list_of_words.count(a)

print(set_of_words)

