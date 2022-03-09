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
frequency = dict()
for word in user_input.split():
    count = frequency.get(word, 0)
    frequency[word] = count+1
    print(word, ":", frequency[word])