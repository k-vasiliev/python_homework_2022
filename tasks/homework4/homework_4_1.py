"""
Оформите решение задачи 3.5 (про поиск чисел Фибоначи) в виде функции
Она должна возвращать список из чисел. Используйте типизацию!
"""


def fib(num_of_elements: int, final_list: list):
    argument1 = 1
    argument2 = 0
    for _ in range(0, num_of_elements):
        summa = argument1 + argument2
        argument1 = argument2
        argument2 = summa
        final_list.append(summa)
    return final_list


print(fib(20, []))
