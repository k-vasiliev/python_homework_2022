"""
Оформите решение задачи 3.5 (про поиск чисел Фибоначи) в виде функции
Она должна возвращать список из чисел. Используйте типизацию!
"""


def fibonacci(n: int):
    fib = [1, 1]
    for _ in range(1, n-1):
        fib_n = int(fib[-2]) + int(fib[-1])
        fib.append(fib_n)
    return fib


n_input = int(input())
print(*fibonacci(n_input), sep = ', ')
