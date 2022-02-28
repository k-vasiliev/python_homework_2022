"""

Пользователь вводит строку, состоящая из слов

Сделайте из нее аббревиатуру с помощью list comprehension и распечатайте

Вход: "Комитет Государственной Безопасности"
Выход: "КГБ"

"""

input_string = (input())
input_list = input_string.split(' ')
abbr = [word[0].upper() for word in input_list]
print(*abbr, sep='')