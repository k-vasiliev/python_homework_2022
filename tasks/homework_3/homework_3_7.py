"""

Пользователь вводит строку, состоящая из слов

Сделайте из нее аббревиатуру с помощью list comprehension и распечатайте

Вход: "Комитет Государственной Безопасности"
Выход: "КГБ"

"""

input_string = (input())
new = [i for i in input_string if i.upper() in i]
print(''.join(map(str, new)))




