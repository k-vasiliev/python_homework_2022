"""

Пользователь вводит строку, состоящая из слов

Сделайте из нее аббревиатуру с помощью list comprehension и распечатайте

Вход: "Комитет Государственной Безопасности"
Выход: "КГБ"

"""

input_string = list(input())
my_list2 = list(input_string[0])
my_list = []
#for i, value in enumerate(input_string):
#    if i == 0:
#        my_list.append(input_string[0])
#    if value == ' ':
#        my_list.append(input_string[i+1])
#print(''.join(map(str, my_list)))


my_list = [input_string[i+1] for i, value in enumerate(input_string) if value == ' ']
print(''.join(map(str, (my_list2)))+''.join(map(str, (my_list))))



