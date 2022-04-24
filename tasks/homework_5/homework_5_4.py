"""
Задача со звездочкой (сложная)

На лекции мы говорили о бинарном поиске - быстром поиске в отсортированном массиве
Напишите функцию, которая реализует этот алгоритм.

Предполагаем, что функция получает на вход всегда отсортированный массив и возвращает индекс элемента
Если элемент не найден, то вернуть None

Не используйте библиотеки, в том числе стандартные

Я рекомендую использовать подход, в котором вы сначала продумываете все пограничные случаи
и используете assert для тестирования

"""


def bisearch(sorted_list: list[int], number_to_find: int):
    mid = len(sorted_list) // 2
    top = len(sorted_list) - 1
    low = 0
    while sorted_list[mid] != number_to_find and low <= top:
        if number_to_find > sorted_list[mid]:
            low = mid + 1
        else:
            top = mid - 1
        mid = (low + top) // 2
    if low > top:
        return None
    else:
        return mid


# assert bisearch([1, 2, 3], 2) == 1
# assert bisearch([1, 2, 3], 5) is None
print(bisearch([1, 2, 3], 3))
