"""
Оформите решение задачи 3.5 (про поиск чисел Фибоначи) в виде функции
Она должна возвращать список из чисел. Используйте типизацию!
"""


def Fibonachi_list(N: int) -> list:
    fib_element1 = 1
    fib_element2 = 1
    result_list = list()
    result_list.append(fib_element1)  # минимум один элемент

    # Если больше одного элемента, то запускаем процесс поиска
    if N > 1:
        result_list.append(fib_element2)

        # последующие элементы ищем итерационно
        for i in range(2, N):
            # считаем следующий элемент ряда
            fib_element1, fib_element2 = fib_element2, fib_element1 + fib_element2
            # добавляем элемент в список
            result_list.append(fib_element2)
    return result_list


# запрашиваем число N
N = int(input())

fib_list = Fibonachi_list(N)

# выдаем результат в запрошенном формате
print(str(fib_list)[1:-1])
