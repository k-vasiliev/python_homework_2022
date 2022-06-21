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

ans_shops = {}

for i in shops:
    temp_line = {i['товар']: i['количество']}
    for key in temp_line:
        if key not in ans_shops:
            ans_shops.update(temp_line)
        else:
            ans_shops.update({key: (temp_line[key] + ans_shops[key])})
print(ans_shops)

for keys, value in ans_shops.items():
    print(f'{keys} : {value}')
