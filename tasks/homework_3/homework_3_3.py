"""
Найти все числа от 1000 до 3000 включительно, все цифры которых четные.
Программа должна выдавать результат в виде разделенной запятыми строки

"""
new_list = []
new_list2 = []

for i in range(200, 301):
    if i % 2 == 0:
        new_list.append(i)
for j in new_list:
    if all(int(digit) % 2 == 0 for digit in str(j)):
        new_list2.append(j)
print(new_list2)










