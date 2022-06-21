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


def bisearch(sorted_list: list[int], number_to_find) -> int:
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        middle = low + (high - low) // 2

        if sorted_list[middle] == number_to_find:
            return middle
        elif sorted_list[middle] < number_to_find:
            low = middle + 1
        else:
            high = middle - 1


assert bisearch([1, 2, 3], 2) == 1
assert bisearch([1, 2, 3], 5) is None
assert bisearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10) is None
assert bisearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 3) == 3
assert bisearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 9) == 9
# рекомендую дописать сюда еще проверок функций на пограничные ситуации
