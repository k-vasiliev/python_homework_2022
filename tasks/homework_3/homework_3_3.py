"""
Найти все числа от 1000 до 3000 включительно, все цифры которых четные.
Программа должна выдавать результат в виде разделенной запятыми строки

"""

list_divs = []
list_of_nums = list(range(1000,3001))
for element in list_of_nums:
    if element % 2 == 0 and element // 10 % 2 == 0 and element // 100 % 2 == 0 and element // 1000 % 2 == 0:
        list_divs.append(element)
print (list_divs)




