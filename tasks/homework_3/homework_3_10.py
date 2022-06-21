"""

Дан список из tuple - пар координат x и y
Найдите две точки, расстояние между которыми минимальное. Выведите их через запятую

Вывод:
(1, 5),(3, 8)

"""
from math import sqrt
points = [(1, 3), (5, 9), (0, 2), (15, 1), (17, 2), (0, 5), (2, 9)]

points_dict = {}
min_p1 = 0
min_p2 = 1
distant_min = sqrt((points[0][0] - points[1][0]) ** 2 + (points[0][1] - points[1][1]) ** 2)

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i]
        x2, y2 = points[j]
        distant = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if distant_min > distant:
            distant_min = distant

            print(f'{points[i]},{points[j]}')







