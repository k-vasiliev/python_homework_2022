"""

Пользователь вводит строку, состоящая из слов

Сделайте из нее аббревиатуру с помощью list comprehension и распечатайте

Вход: "Комитет Государственной Безопасности"
Выход: "КГБ"

"""

input_string = (input())

words = input_string.split(" ")

words_abb = [words[0] for words in words]

print(''.join(list(map(str, words_abb))))
