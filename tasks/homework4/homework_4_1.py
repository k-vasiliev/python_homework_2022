"""
Оформите решение задачи 3.5 (про поиск чисел Фибоначи) в виде функции
Она должна возвращать список из чисел. Используйте типизацию!
"""
user_var = int(input())
#Пользователь задает количство чисел

def fibonacci(n: int) -> list:
    user_list = [1, 1]

    i = 0

    while i <= n - 3:
        x = user_list[i] + user_list[i + 1]

        user_list.append(x)

        i += 1
    return user_list


print(fibonacci(user_var))
