"""
Оформите решение задачи 3.5 (про поиск чисел Фибоначи) в виде функции
Она должна возвращать список из чисел. Используйте типизацию!
"""


def fibo_numbers(num_values: int):
    start_num = 0
    next_num = 1
    list_of_nums = [next_num]
    for x in range(num_values - 1):
        print_num = start_num + next_num
        start_num = next_num
        next_num = print_num
        list_of_num.append(list_of_nums)
    return print(list_of_num)


fibo_numbers(8)
