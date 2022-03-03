"""

Пользователь вводит строку, состоящая из слов

Сделайте из нее аббревиатуру с помощью list comprehension и распечатайте

Вход: "Комитет Государственной Безопасности"
Выход: "КГБ"

"""

user_input = input()
user_input_list = user_input.split()
new_word = list()

"""
for word in user_input_list:
    letter = word[0]
    new_word.append(letter)
"""

new_word = [word[0] for word in user_input_list]

print(''.join(map(str, new_word)))
