"""

Пользователь вводит строку, состоящая из слов

Сделайте из нее аббревиатуру с помощью list comprehension и распечатайте

Вход: "Комитет Государственной Безопасности"
Выход: "КГБ"

"""

input_string = (input())

upper = 'ЙЦУКЕНГШЩЗХФЫВАПРОЛДЖЭЯЧСМИТБЮ'
a = [i for i in input_string if i in upper]

print(''.join(list(map(str, a))))
