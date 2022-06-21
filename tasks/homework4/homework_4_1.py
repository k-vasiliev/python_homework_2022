"""
Оформите решение задачи 3.5 (про поиск чисел Фибоначи) в виде функции
Она должна возвращать список из чисел. Используйте типизацию!
"""

def fibonacci(User_number_input: int) -> list:
    first_two_fibonacci_numbers = [1, 1]
    for i in range(1, User_number_input-1):
        fib_n = int(first_two_fibonacci_numbers[-2]) + int(first_two_fibonacci_numbers[-1])
        first_two_fibonacci_numbers.append(fib_n)
    return first_two_fibonacci_numbers

User_number_input = int(input())
print(*fibonacci(User_number_input), sep = ', ')