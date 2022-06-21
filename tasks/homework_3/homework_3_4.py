"""

Дан список из словарей
Напишите программу, которая объединяет значения в один словарь
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
    {'товар': 'яблоки', 'количество': 750}
]

# ваш код

result_dictionary = {}

goods_count = 0
new_goods_count = 0
goods = ''
for i in shops:
    if i['товар'] in result_dictionary:
        for j in result_dictionary:
            if j == i['товар']:
                new_goods_count = result_dictionary[j]
        new_goods_count = new_goods_count + i['количество']
        result_dictionary[i['товар']] = new_goods_count
    else:
        goods = i['товар']
        goods_count = i['количество']
        result_dictionary[goods] = goods_count
print(result_dictionary)
