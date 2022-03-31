"""
Оформите решение задачи 3.5 (про поиск чисел Фибоначи) в виде функции
Она должна возвращать список из чисел. Используйте типизацию!
"""
user_input = int(input('Ввести число: '))
def fib(n):
    if n in {0, 1, 2}:
        return n
    return fib(n - 1) + fib(n - 2)
print([fib(n) for n in range(user_input)])