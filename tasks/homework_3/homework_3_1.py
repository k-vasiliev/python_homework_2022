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
# привет как дела что здесь что как
user_input = input("Введите фразу: ")
words = user_input.split()
wordsdict = {}
for word in words:
    word = word.lower()
    if word not in wordsdict:
        wordsdict[word] = 1
    else:
        wordsdict[word] = wordsdict[word] + 1
print(wordsdict)

