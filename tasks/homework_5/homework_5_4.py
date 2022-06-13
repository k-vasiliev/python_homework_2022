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
    l = len(sorted_list)
    ml = l // 2
    m_start = 0

    while len(sorted_list) != 1:
        #уходим в левую часть массива
        if number_to_find < sorted_list[ml]:
            sorted_list = sorted_list[:ml]
            l = len(sorted_list)
            ml = l // 2
            print(sorted_list)
        #уходим в правую часть массива
        else:
            sorted_list = sorted_list[ml:]
            l = len(sorted_list)
            m_start = m_start + ml
            ml = l // 2
            print(sorted_list)
    if sorted_list[0] != number_to_find:
        return None
    return m_start

print(bisearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 10))

# assert bisearch([1, 2, 3], 3) == 2
# assert bisearch([1, 2, 3], 5) is None
# assert bisearch([-1, 2, 3], -1) == 0
# assert bisearch([-1, 0, 2, 3, 19], 19) == 4
# assert bisearch([1, 1, 1, 2, 3, 4], 1) == 2 #можно упороться, чтобы находило первое вхождение искомого числа, но кажется это избыточно, если нужно было так - пиши
# рекомендую дописать сюда еще проверок функций на пограничные ситуации
