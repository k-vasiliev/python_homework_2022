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
        # печатаем все аргументы функции, на которой была вызвана
        print(args, kwargs)
        start_time = datetime.datetime.now()  # Засекли время начала выполнения
        res = func(*args, **kwargs)  # Запустили
        # печатаем время начала и окончания работы функции
        print(f"Начало работы {start_time}, конец работы {datetime.datetime.now()}")
        # печатаем результат работы функции
        print(res)
        return res

    return wrapper


# к этой функции надо применить декоратор
@debug
def example_function(argument):
    return argument[::-1]


example_function("Hello! Debug me, please")
