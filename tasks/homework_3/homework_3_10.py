"""

Дан список из tuple - пар координат x и y
Найдите две точки, расстояние между которыми минимальное. Выведите из через запятую

Вывод:
(1, 5),(3, 8)

"""

points = [(1, 3), (5, 9), (0, 2), (15, 1), (17, 2), (0, 5), (2, 9)]

distances_dictionaries = []

for x1, y1 in points:
    for x2, y2 in points:
        if x1 != x2 and y1 != y2:
            d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            distances_dictionaries.append({((x1, y1), (x2, y2)): d})

distances_values_list = []

for dictionary in distances_dictionaries:
    for key in dictionary:
        distances_values_list.append(dictionary.get(key))

min_distance = min(distances_values_list)

index_min_distance = distances_values_list.index(min_distance)

res_points = list(distances_dictionaries[index_min_distance].keys())

first_point = res_points[0][0]
second_point = res_points[0][1]

print(first_point, second_point, sep=', ')
