import re
from datetime import datetime

"""
Напишите функцию-декоратор debug, которая:
* печатает все аргументы функции, на которой была вызвана
* печатает время начала и окончания работы функции
* печатает результат работы функции

Примените декоратор к example_function
"""


def debug(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        start_time_to_str = re.search(r'\s\d+\:\d+\:\d+\.\d+', str(start_time))  # просто практика, знаю что можно
        # оптимальней
        print("Время начала работы функции: {} ".format(start_time_to_str.group(0)))
        res = func(*args, **kwargs)
        end_time = datetime.now()
        end_time_to_str = re.search(r'\s\d+\:\d+\:\d+\.\d+', str(end_time))
        print("Время окончания работы функции: {} ".format(end_time_to_str.group(0)))
        print('Аргументы функции: {}'.format(*args))
        print('Результат работы функции: {}'.format(res))
        return res

    return wrapper


@debug
def example_function(argument):
    return argument[::-1]


example_function("Hello!Debug me, please")
example_function("Hello, what is wrapper?")
