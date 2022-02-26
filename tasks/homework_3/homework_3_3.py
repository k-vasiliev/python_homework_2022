"""
Найти все числа от 1000 до 3000 включительно, все цифры которых четные.
Программа должна выдавать результат в виде разделенной запятыми строки

"""
list_1 = []
for i in range(1000, 3001):
    i = str(i)
    is_correct = True
    for j in i:
        j = int(j)
        if j % 2 != 0:
            is_correct = False
    if is_correct:
        list_1.append(i)
result = ','.join(list_1)
print(result)
