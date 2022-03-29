"""
Оформите решение задачи 3.5 (про поиск чисел Фибоначи) в виде функции
Она должна возвращать список из чисел. Используйте типизацию!
"""

N = int(input())


def fibonacci_of(n):
    if n in {0, 1}:
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


print([fibonacci_of(n) for n in range(N)])

