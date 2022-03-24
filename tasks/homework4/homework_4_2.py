"""
Напишите функцию-декоратор debug, которая:
* печатает все аргументы функции, на которой была вызвана
* печатает время начала и окончания работы функции
* печатает результат работы функции

Примените декоратор к example_function
"""


def debug(func):
    import datetime
    def wrapper(*args, **kwargs):
        print(f"Function's arguments: ", end='')
        print(*args)
        print(f"Start func: {datetime.datetime.now()}")
        print("Function's result: ", end='')
        func(*args, **kwargs)
        print(f"End func: {datetime.datetime.now()}")
    return wrapper

# к этой функции надо применить декоратор


def example_function(argument):
    return print(argument[::-1])


example_function = debug(example_function)


print_example_function = example_function("Hello! Debug me, please")

