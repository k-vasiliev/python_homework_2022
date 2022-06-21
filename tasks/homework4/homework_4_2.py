"""
Напишите функцию-декоратор debug, которая:
* печатает все аргументы функции, на которой была вызвана
* печатает время начала и окончания работы функции
* печатает результат работы функции

Примените декоратор к example_function
"""


def debug(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('время начала: {} секунд, время окончания: {}'.format(end, start))
        return return_value
    return wrapper

# к этой функции надо применить декоратор
@debug
def example_function(argument):
    return argument[::-1]


print(example_function("Hello! Debug me, please"))
