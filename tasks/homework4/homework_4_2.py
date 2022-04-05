"""
Напишите функцию-декоратор debug, которая:
* печатает все аргументы функции, на которой была вызвана
* печатает время начала и окончания работы функции
* печатает результат работы функции

Примените декоратор к example_function
"""
import time


def debug(func):
    pass

    def wrapper(*args):
        print(*args)
        print(time.perf_counter()) #t start
        print(func(*args))
        print(time.perf_counter()) #t end
    return wrapper

# к этой функции надо применить декоратор
@debug
def example_function(argument):
    return argument[::-1]


example_function("Hello! Debug me, please")
