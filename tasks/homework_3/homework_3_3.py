"""
Найти все числа от 1000 до 3000 включительно, все цифры которых четные.
Программа должна выдавать результат в виде разделенной запятыми строки

"""
all_even = []
for n in (1000, 1001):
    n_list = [int(a) for a in str(n)]
    for elem in n_list:
        if elem % 2 != 0:
            break
    all_even.append(n)
print(all_even)



