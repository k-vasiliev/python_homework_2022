"""

Дан список из tuple - пар координат x и y
Найдите две точки, расстояние между которыми минимальное. Выведите из через запятую

Вывод:
(1, 5),(3, 8)

"""
import math

points = [(1, 3), (5, 9), (0, 2), (15, 1), (17, 2), (0, 5), (2, 9)]
counter = 0
x0 = float("inf")

while counter < len(points):
    dot1 = points[counter]
    counter += 1
    for dot in points:
        if dot != dot1:
            x = math.dist(dot1, dot)
            if x < x0:
                x0 = x
                a = dot1
                b = dot
print(f'{a},{b}')
