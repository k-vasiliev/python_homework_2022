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

user_input = input().lower()
word_list = user_input.split(' ')

# список уникальных слов
unique_word = []
for w in word_list:
    if w in unique_word:
        continue
    else:
        unique_word.append(w)

# составим список из списков "слово, количество"
count_word = []

for word in unique_word:
    count_word.append([word, word_list.count(word)])

for i, j in count_word:
    print(f'{i}: {j}')


