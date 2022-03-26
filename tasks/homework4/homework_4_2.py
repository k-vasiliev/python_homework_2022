"""
Напишите функцию-декоратор debug, которая:
* печатает все аргументы функции, на которой была вызвана
* печатает время начала и окончания работы функции
* печатает результат работы функции

Примените декоратор к example_function
"""

def debug(func):
    import time
    def wrapper(func_arg):
        print('Аргумент(ы) функции: {}'.format(func_arg))
        func_start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        function_result = func(func_arg)
        func_end_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        print(f'Время начала работы фунукции: {func_start_time} \nВремя окончания работы фунукции: {func_end_time}')
        print(f'Результат работы функции: {function_result}')
    return wrapper

# к этой функции надо применить декоратор
@debug
def example_function(argument):
    return argument[::-1]


example_function("Hello! Debug me, please")

