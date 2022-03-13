"""

Дан список из tuple - пар координат x и y
Найдите две точки, расстояние между которыми минимальное. Выведите из через запятую

Вывод:
(1, 5),(3, 8)

"""
from math import dist
from itertools import combinations

points = [(1, 3), (5, 9), (0, 2), (15, 1), (17, 2), (0, 5), (2, 9)]
result = max(dist(x, y) for x, y in combinations(points, 2))
print(result)