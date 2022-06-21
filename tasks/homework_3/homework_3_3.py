"""
Найти все числа от 1000 до 3000 включительно, все цифры которых четные.
Программа должна выдавать результат в виде разделенной запятыми строки

"""

list_of_even_numbers = []
list_of_even_numbers_and_digits = []

for i in range(2000, 2020):
    if i % 2 == 0:
        list_of_even_numbers.append(i)

for a in list_of_even_numbers:
    if all(int(digit_in_number) % 2 == 0 for digit_in_number in str(a)):
        list_of_even_numbers_and_digits.append(a)

print(list_of_even_numbers_and_digits)
