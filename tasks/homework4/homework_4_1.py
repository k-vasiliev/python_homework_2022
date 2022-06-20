"""
Оформите решение задачи 3.5 (про поиск чисел Фибоначи) в виде функции
Она должна возвращать список из чисел. Используйте типизацию!
"""
x = int(input())
def get_fibonacci(n):
    f1 = 1
    f2 = 1
    i = 2
    new_list = [1, 1]
    if n >= 2:
        while i < n:
            summa = f1 + f2
            f1 = f2
            f2 = summa
            i += 1
            new_list.append(summa)
        return new_list


a = get_fibonacci(x)
print(a)