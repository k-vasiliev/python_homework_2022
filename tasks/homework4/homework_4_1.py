"""
Оформите решение задачи 3.5 (про поиск чисел Фибоначи) в виде функции
Она должна возвращать список из чисел. Используйте типизацию!
"""

def fibonacci(N: int) -> list:
    f1, f2 = 1, 1
    for i in range(N):
        yield f1
        f1, f2 = f2, f1 + f2

result = list(fibonacci(int(input("Введите число: "))))
print(result)
