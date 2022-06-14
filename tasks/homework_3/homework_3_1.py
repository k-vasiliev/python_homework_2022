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
import string
user_input = str(input().lower())

#Убираем знаки препинания
for i in string.punctuation:
    if i in user_input:
        user_input = user_input.replace(i, '')

user_input = user_input.split(" ")

#Создаем список из слов в строке
list_of_words = []
for i in user_input:
    if i not in list_of_words:
        list_of_words.append(i)
        #print(list_of_words)

#Считаем кол-во уникальных слов и выводим результат
for i in range(0, len(list_of_words)):
    count_user_input = user_input.count(list_of_words[i])
    print(f"{list_of_words[i]}:{count_user_input}")
