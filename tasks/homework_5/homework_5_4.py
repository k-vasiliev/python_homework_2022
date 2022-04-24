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

def bisearch(list_of_numbers, number) -> int:
    lenght = len(list_of_numbers)
    mid_count = 0
    count = 0
    if lenght == 0:
        print('None')
    elif lenght > 0:
        while len(list_of_numbers) >= 1:
            mid = len(list_of_numbers) // 2
            if number == list_of_numbers[mid]:
                if mid_count == 0:
                    print(mid)
                    break
                else:
                    print(mid_count + mid + count)
                    break
            elif number > list_of_numbers[mid]:
                list_of_numbers = list_of_numbers[mid + 1:]
                mid_count += mid
                count += 1
            elif number < list_of_numbers[mid]:
                list_of_numbers = list_of_numbers[:mid]
        else:
            print('None')
    return

bisearch([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
#bisearch([1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711], 20000)
