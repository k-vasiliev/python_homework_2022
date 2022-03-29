"""

Дан список из tuple - пар координат x и y
Найдите две точки, расстояние между которыми минимальное. Выведите из через запятую

Вывод:
(1, 5),(3, 8)

"""

points = [(1, 3), (5, 9), (0, 2), (15, 1), (17, 2), (0, 5), (2, 9)]

import math
from math import hypot
from math import dist
points_int = list(int(points))
minimum = float("inf")
for x1, x2 in points:
    if min(dist(x1, x2)) < minimum:
        print(x1)




