"""

Дан список из tuple - пар координат x и y
Найдите две точки, расстояние между которыми минимальное. Выведите из через запятую

Вывод:
(1, 5),(3, 8)

"""

points = [(1, 3), (5, 9), (0, 2), (15, 1), (17, 2), (0, 5), (2, 9)]
max_p = max(points)
min_p = min(points)
max_dist = ((max_p[0] - min_p[0])**2 + (max_p[1] - min_p[1])**2)**0.5
min_dist = max_dist
for point in points:
        print(points[point], point[1])

"""for x, y in points:
    for x1, y1 in points:
        if x != x1 and y != y1:
            s = pow((pow((x1 - x), 2) + pow((y1 - y), 2)), 0.5)
            if s < min_dist:
                min_dist = s
                min_dist_points = [(x, y), (x1, y1)]
                print(min_dist)
                print(min_dist_points)
"""
