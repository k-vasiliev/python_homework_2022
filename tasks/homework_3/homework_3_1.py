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

list_user = user_input.split()
one_list = []
for i in list_user:
    if i not in one_list:
        one_list.append(i)
for i in range(0, len(one_list)):
    print(one_list[i], ':', list_user.count(one_list[i]))

