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

# Разделяем фразу на слова
splitted_string = user_input.split(' ')

# Находим множество слов во фразе
words = set(splitted_string)

# Проходим по множеству слов и выводим частоту упоминания
for word in words:
    count = splitted_string.count(word)
    print(f"{word}:{count}")
