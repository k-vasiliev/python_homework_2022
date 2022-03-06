"""

Пользователь вводит строку, состоящую из чисел, разделенных пробелом
Используя циклы, найдите наибольшее и наименьшее число в этом списке

Не используйте стандартные функции min и max!

Вход: 10 8 3 15
Выход:
Наибольшее число: 15
Наименьшее число: 3

"""

user_input = input()
user_list = user_input.split()


def large(user):
    list_user = list(user.split())
    max_ = int(list_user[0])
    for element in list_user:
        if int(element) > max_:
            max_ = element

    return max_


def large_min(user):
    list_user_min = list(user.split())
    min_ = int(list_user_min[0])
    for element_min in list_user_min:
        if int(element_min) < int(min_):
            min_ = element_min

    return min_


result = large(user_input)
result_min = large_min((user_input))
print(result, result_min)
