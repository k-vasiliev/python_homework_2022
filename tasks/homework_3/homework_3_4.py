"""

Напишите программу, которая объединяет значения из двух списков.
Структура всегда одна и та же - товар и количество

Ввод:

shops = [
    {'товар': 'яблоки', 'количество': 400},
    {'товар': 'конфеты', 'количество': 300},
    {'товар': 'яблоки', 'количество': 750}
]
Вывод:

{'яблоки': 1150, 'конфеты': 300}

"""

shops = [
    {'товар': 'яблоки', 'количество': 400},
    {'товар': 'конфеты', 'количество': 300},
    {'товар': 'яблоки', 'количество': 150}
]

result = dict()
list_values = []
list_keys = []
for i in range(len(shops)):
    y = list(shops[i].values())[0]
    list_keys.append(y)
    x = list(shops[i].values())
    list_values.append(x)
result_dict = result.fromkeys(list_keys, 0)
for i in list_values:
    for j in result_dict:
        if i[0] == j:
            result_dict[j] += i[1]

print(result_dict)
