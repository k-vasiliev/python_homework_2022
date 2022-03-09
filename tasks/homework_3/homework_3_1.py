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
from collections import Counter
str_input = input("Вход: ")
arg = Counter(str_input.split()).most_common()

for word, count in arg:
    print(word,":",count)