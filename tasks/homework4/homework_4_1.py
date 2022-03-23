"""
Оформите решение задачи 3.5 (про поиск чисел Фибоначи) в виде функции
Она должна возвращать список из чисел. Используйте типизацию!
"""

N = int(input())


def get_fibonacci(n: int) -> list:
    """
    Функция для нахождения последовательности Фибоначи
    :param n: число, введёное пользователем
    :return: список из последовательности Фибоначи,
    в котором количество элементов соответствует введённому пользователем числу
    """
    number1 = 1
    number2 = 1
    fib_list = [number1]
    for i in range(2, n + 1):
        number2, number1 = number1, number2 + number1
        fib_list.append(number2)
    return fib_list


print(get_fibonacci(N))
