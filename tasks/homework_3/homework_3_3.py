"""
Найти все числа от 1000 до 3000 включительно, все цифры которых четные.
Программа должна выдавать результат в виде разделенной запятыми строки

"""

itog_list_of_number = list()

for number in range(1000, 3001):
    number_list = list(str(number))
    test_list = list()
    for n in number_list:
        if int(n) % 2 == 0:
            test_list.append(n)
        if len(test_list) == len(number_list):
            itog_list_of_number.append(number)

print(', '.join(map(str, itog_list_of_number)))
