"""
Найти все числа от 1000 до 3000 включительно, все цифры которых четные.
Программа должна выдавать результат в виде разделенной запятыми строки

"""


def check_even(num):
    while num > 0:
        if num % 2 == 0:
            num //= 10
        else:
            return False
    return True


array_of_ans = []
for i in range(1000, 3000, 2):
    if check_even(i):
        array_of_ans.append(i)

print(array_of_ans)
