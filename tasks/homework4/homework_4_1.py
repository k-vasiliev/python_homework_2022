"""
Оформите решение задачи 3.5 (про поиск чисел Фибоначи) в виде функции
Она должна возвращать список из чисел. Используйте типизацию!
"""

def fibonacci(N):
    f1 = 1
    f2 = 1
    fibonacci_numbers = [1, 1]
    if N in (1, 2):
        print(fibonacci_numbers[:N])
    else:
        while len(fibonacci_numbers) < N:
            fn = f1 + f2
            fibonacci_numbers.append(fn)
            f1 = f2
            f2 = fn
        print(fibonacci_numbers[:N])

N = int(input())
fibonacci(N)
