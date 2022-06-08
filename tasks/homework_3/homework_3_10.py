"""

Дан список из tuple - пар координат x и y
Найдите две точки, расстояние между которыми минимальное. Выведите из через запятую

Вывод:
(1, 5),(3, 8)

"""
from math import sqrt

points = [(1, 3), (5, 9), (0, 2), (15, 1), (17, 2), (0, 5), (2, 9)]


def dot_distance(dot_1: tuple(), dot_2: tuple()):
    x_1 = dot_1[0]
    y_1 = dot_1[1]

    x_2 = dot_2[0]
    y_2 = dot_2[1]
    distance = sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
    return distance


min_dist = float('+inf')

dot_ans_1 = tuple()
dot_ans_2 = tuple()

for i in range(len(points) - 1):
    for x in range(i + 1, len(points)):
        if dot_distance(points[i], points[x]) < min_dist:
            min_dist = dot_distance(points[i], points[x])
            dot_ans_1 = points[i]
            dot_ans_2 = points[x]

print(dot_ans_1, dot_ans_2)


