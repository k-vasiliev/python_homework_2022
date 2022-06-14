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
        print(*args)
        print(datetime.now())
        print(func(*args))
        print(datetime.now())
    return wrapper

# к этой функции надо применить декоратор

@debug
def example_function(argument):
    return argument[::-1]


example_function("Hello! Debug me, please")