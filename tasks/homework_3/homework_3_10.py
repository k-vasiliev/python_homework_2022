"""
Дан список из tuple - пар координат x и y
Найдите две точки, расстояние между которыми минимальное. Выведите из через запятую
Вывод:
(1, 5),(3, 8)
"""
import math
points = [(1, 3), (5, 9), (0, 2), (15, 1), (17, 2), (0, 5), (2, 9)]
xy = 0
minimum = None
first_point = (0, 0)
second_point = (0, 0)
for i in range(len(points)):
    for j in range(len(points)):
        if i != j:
            xy = math.sqrt(math.pow(points[j][0] - points[i][0], 2) + math.pow(points[j][1] - points[i][1], 2))
            if minimum is None or xy < minimum:
                minimum = xy
                first_point, second_point = points[i], points[j]
print(first_point, second_point)
