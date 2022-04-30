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
    search_index = 0
    loop_counter = 0
    while len(sorted_list) >= 1:
        if len(sorted_list) > 1:
            middle_index = (len(sorted_list) // 2 + len(sorted_list) % 2) - 1
        else:
            middle_index = 0
        if sorted_list[middle_index] == number_to_find:
            if loop_counter == 0:
                search_index = middle_index
            else:
                search_index += middle_index + 1
            return search_index
        elif len(sorted_list) == 1:
            return None
        elif sorted_list[middle_index] > number_to_find:
            sorted_list = sorted_list[:middle_index]
        elif sorted_list[middle_index] < number_to_find:
            sorted_list = sorted_list[middle_index + 1:]
            if loop_counter == 0:
                search_index = middle_index
            else:
                search_index += middle_index + 1
            loop_counter += 1
print(bisearch([1, 1, 1, 1, 3, 4, 5, 6, 8, 9, 10, 10, 10], 1))
