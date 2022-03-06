"""

Дан список из tuple - пар координат x и y
Найдите две точки, расстояние между которыми минимальное. Выведите их через запятую

Вывод:
(1, 5),(3, 8)

"""

points = [(1, 3), (5, 9), (0, 2), (15, 1), (17, 2), (0, 5), (2, 9)]

from math import sqrt

x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))

def distance(x1, y1, x2, y2):
    c = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return c
c = distance(x1, y1, x2, y2)
print(c)

#прошу подсказки!




