"""

Пользователь вводит строку, состоящая из слов

Сделайте из нее аббревиатуру с помощью list comprehension и распечатайте

Вход: "Комитет Государственной Безопасности"
Выход: "КГБ"

"""

input_string = (input())

list1 = list(input_string.split(' '))
list_out = list()

for element in list1:
    list2 = list(element)
    list_out.append(list2[0])

output = ''.join(list_out)
print(output)
