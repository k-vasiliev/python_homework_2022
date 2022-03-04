"""

Дан список из tuple - пар координат x и y
Найдите две точки, расстояние между которыми минимальное. Выведите из через запятую

Вывод:
(1, 5),(3, 8)

"""

from math import sqrt

points = [(1, 3), (5, 9), (0, 2), (15, 1), (17, 2), (0, 5), (2, 9)]

a = points[0]
b = points[1]
min_distance = sqrt(abs((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2))

for one_element in points:
    for another_element in points:
        if one_element != another_element:
            distance = sqrt(abs((another_element[0] - one_element[0]) ** 2 + (another_element[1] - one_element[1]) ** 2))
            if distance < min_distance:
                min_distance = distance
                a = one_element
                b = another_element

print(f"{a},{b}")
