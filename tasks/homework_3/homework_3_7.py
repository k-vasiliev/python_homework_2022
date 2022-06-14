"""

Пользователь вводит строку, состоящая из слов

Сделайте из нее аббревиатуру с помощью list comprehension и распечатайте

Вход: "Комитет Государственной Безопасности"
Выход: "КГБ"

"""

user_input_string = input().split()
list_of_input = list()

for i in user_input_string:
    list_of_input.append(i[0])

list_of_input = ''.join(map(str, list_of_input))

print(list_of_input)