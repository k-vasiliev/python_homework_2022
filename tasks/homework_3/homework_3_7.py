"""

Пользователь вводит строку, состоящая из слов

Сделайте из нее аббревиатуру с помощью list comprehension и распечатайте

Вход: "Комитет Государственной Безопасности"
Выход: "КГБ"

"""

input_string = input().split()
input_list = list()

for i in input_string:
    input_list.append(i[0])


input_list = ''.join(map(str, input_list))

print(input_list)

