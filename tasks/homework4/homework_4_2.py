"""
Напишите функцию-декоратор debug, которая:
* печатает все аргументы функции, на которой была вызвана
* печатает время начала и окончания работы функции
* печатает результат работы функции
Примените декоратор к example_function
"""

def debug(func):
    pass

    import datetime
    def wrapper (*args, **kwargs):
        print(*args, **kwargs)
        print("Start:", datetime.datetime.now())
        func(*args, **kwargs)
        print("Finish:", datetime.datetime.now())
        print("Debug result:", func(*args, **kwargs))
    return wrapper

# к этой функции надо применить декоратор
@debug
def example_function(argument):
    return argument[::-1]

example_function("Hello! Debug me, please")

