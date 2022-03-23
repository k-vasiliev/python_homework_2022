"""

Дан список из tuple - пар координат x и y
Найдите две точки, расстояние между которыми минимальное. Выведите из через запятую

Вывод:
(1, 5),(3, 8)

"""

points = [(1, 3), (5, 9), (0, 2), (15, 1), (17, 2), (0, 5), (2, 9)]

# найдем расстояние между первой и второй точкой и скажем, что оно минимальное
point_1 = points[0]
point_2 = points[1]
dist_min = ((point_1[0] - point_2[0]) ** 2 + (point_1[1] - point_2[1]) ** 2) ** 0.5
# найдем расстояние между каждой парой точек. Если оно меньше dist_min, то оно минимально в этой итерации
for tup1 in points:
    for tup2 in points:
        if tup1 != tup2:
            dist = ((tup1[0] - tup2[0]) ** 2 + (tup1[1] - tup2[1]) ** 2) ** 0.5
            if dist < dist_min:
                dist_min = dist
                points_min_dist = [tup1, tup2]
print(f'{points_min_dist[0]},{points_min_dist[1]}')
