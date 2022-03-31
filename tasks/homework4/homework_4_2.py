"""
Напишите функцию-декоратор debug, которая:
* печатает все аргументы функции, на которой была вызвана
* печатает время начала и окончания работы функции
* печатает результат работы функции
Примените декоратор к example_function
"""
import datetime
def debug(func):
    def wrapper(*args):
        print(*args)
        print(f'Start: {datetime.datetime.now()}')
        print(f'Finish: {datetime.datetime.now()}')
        print(func(*args))
    return wrapper
@debug
def example_function(argument):
    return argument[::-1]
example_function("Hello, world!")