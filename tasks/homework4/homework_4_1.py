"""
Оформите решение задачи 3.5 (про поиск чисел Фибоначи) в виде функции
Она должна возвращать список из чисел. Используйте типизацию!
"""

# Используйте типизацию! - Ок! ¯\_(ツ)_/¯

def fibonacci(N: int) -> list:
    #беру свое же решение
    my_list = [0]
    for i in range(N):
        if len(my_list) == 1:
            my_list.append(i + 1)
        else:
            x = my_list[i - 1] + my_list[i]
            my_list.append(x)
    return print(my_list[1:]) # возвращаем список из чисел

user_intput = int(input()) #пользователь указывает длину списка чисел Фибоначчи

fibonacci(user_intput) #функция возвращает то, что хочет пользователь:)
