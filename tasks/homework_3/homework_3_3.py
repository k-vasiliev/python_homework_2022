"""
Найти все числа от 1000 до 3000 включительно, все цифры которых четные.
Программа должна выдавать результат в виде разделенной запятыми строки

"""
number = 1000
last_number = 3000

even_numbers = []
while number <= last_number:
    if number % 2 == 0:
        even_numbers.append(number)
    number += 1

even_numbers_str_items = list(map(str, even_numbers))

print(', '.join(even_numbers_str_items))
