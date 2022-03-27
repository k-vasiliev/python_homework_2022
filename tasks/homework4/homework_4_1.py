"""
Оформите решение задачи 3.5 (про поиск чисел Фибоначи) в виде функции
Она должна возвращать список из чисел. Используйте типизацию!
"""

def fibonacci(N: int):
    fibonachi_list = [1, 1]
    if len(fibonachi_list) < N:
        while len(fibonachi_list) < N:
            extra = fibonachi_list[-1] + fibonachi_list[-2]
            fibonachi_list.append(extra)
    elif N == 2:
        fibonachi_list = [1, 1]
    else:
        fibonachi_list = [1]
    return fibonachi_list

N_num = int(input())

print(fibonacci(N_num))