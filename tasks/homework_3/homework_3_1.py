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
split_input = user_input.split(" ")
set_user_input = set(split_input)

for x in set_user_input:
    cnt_words = split_input.count(x)
    print(f"{x}: {cnt_words}")
