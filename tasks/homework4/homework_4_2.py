"""
Напишите функцию-декоратор debug, которая:
* печатает все аргументы функции, на которой была вызвана
* печатает время начала и окончания работы функции
* печатает результат работы функции

Примените декоратор к example_function
"""


def debug(func):
    pass


# к этой функции надо применить декоратор
def example_function(argument):
    return argument[::-1]


example_function("Hello! Debug me, please")
