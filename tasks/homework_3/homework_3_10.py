"""

Дан список из tuple - пар координат x и y
Найдите две точки, расстояние между которыми минимальное. Выведите из через запятую

Вывод:
(1, 5),(3, 8)

"""
import math as m

points = [(1, 3), (5, 9), (0, 2), (15, 1), (17, 2), (0, 5), (2, 9) ] #, (2, 4), (1, 3)]

range_list = []
points_dict = dict()

for i in points:
    for x in points:
        if i != x:
            range_list.append(m.dist(i, x))
            points_dict.update({(i, x): m.dist(i, x)})

min_range = min(range_list)
result_list = []

for i in points_dict.items():
    if i[1] == min_range:
        k = list(i[0])
        k.sort() #т.к. в данном случае повторяющиеся комбинации реверсивны и содержат 2 одинаковых пары точек, то сорт будет работать для них одинаково
        if k not in result_list:
            result_list.append(k)

print(result_list)

#в данной задаче при ином списке точек может быть 2 пары точек с одинаковым минимальным расстоянием
#мои костыли по идее обрабатывают это