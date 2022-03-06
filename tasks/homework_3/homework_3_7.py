"""

Пользователь вводит строку, состоящая из слов

Сделайте из нее аббревиатуру с помощью list comprehension и распечатайте

Вход: "Комитет Государственной Безопасности"
Выход: "КГБ"

"""

input_string = input()
list_user = input_string.split()

list_comp = [n[0] for n in list(list_user)]
print(''.join(list_comp))
