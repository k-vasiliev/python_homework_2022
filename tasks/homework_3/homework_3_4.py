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
final_dict = {}
for dictionary in shops:
    supplement_dict = {dictionary['товар']: dictionary['количество']}
    for position in supplement_dict:
        if position not in supplement_dict:
            final_dict.update(supplement_dict)
        else:
            final_dict.update({position: sum([supplement_dict[position], final_dict[position]])})

print(final_dict)



