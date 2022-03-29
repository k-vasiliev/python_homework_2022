"""
Напишите функцию-декоратор debug, которая:
* печатает все аргументы функции, на которой была вызвана
* печатает время начала и окончания работы функции
* печатает результат работы функции

Примените декоратор к example_function
"""

from datetime import datetime


def debug(func): # это функция-дек, к. принимает какую-то фукнцию func
    def wrapper(*args, **kwargs):
        print("Function started", datetime.now())
        print(func(*args, **kwargs))
        print("Function finished", datetime.now())

    return wrapper


# к этой функции надо применить декоратор
def example_function(argument):
    return argument[::-1]


example_function = debug(example_function)
example_function("Hello! Debug me, please")