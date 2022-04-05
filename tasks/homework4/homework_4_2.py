"""
Напишите функцию-декоратор debug, которая:
* печатает все аргументы функции, на которой была вызвана
* печатает время начала и окончания работы функции
* печатает результат работы функции

Примените декоратор к example_function
"""

from datetime import datetime


def debug(func):
    def wrapper(*args):
        print(*args)    # печатает все аргументы функции, на которой была вызвана
        print(datetime.now())   # печатает время начала работы функции
        function_for_debug = func(*args)     # функция, которую нужно дебажить
        print(datetime.now())   # печатает время окончания работы функции
        print(func(*args))  # печатает результат работы функции
        return function_for_debug
    return wrapper


@debug
def example_function(argument):
    return argument[::-1]


example_function("Hello! Debug me, please")

