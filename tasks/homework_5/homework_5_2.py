"""
В файле data/births-by-mothers-age.csv лежит статистика возрастов рожениц

Ваша задача - написать функцию, которая принимает два года, возрастную группу
и сравнивает изменения в процентах между данными в указанные годы

Пример:
2005, 2006, '25–29'
В 2005 процент женщин попадающих в эту группу - 13797/57747=23.89%
В 2006 процент женщин попадающих в эту группу - 14082/59193=23.78%
Изменение на 0.11%
"""

import csv

total_1_all, total_2_all, total_1_part, total_2_part = 0, 0, 0, 0


def find_mothers_age_diff(year1: int, year2: int, age_group: str):
    global total_1_all, total_2_all, total_1_part, total_2_part
    with open('data/births-by-mothers-age.csv', 'r', newline='') as csv_file:
        reader = csv.reader(csv_file, delimiter=';')
        next(reader)
        for row in reader:
            year_csv = int(row[0])
            if year1 == year_csv and row[1] == 'Total':
                total_1_all = int(row[2])
            elif year2 == year_csv and row[1] == 'Total':
                total_2_all = int(row[2])
            elif year1 == year_csv and row[1] == age_group:
                total_1_part += int(row[2])
            elif year2 == year_csv and row[1] == age_group:
                total_2_part += int(row[2])
        changes_within_group_1 = round(total_1_part / total_1_all, 4) * 100
        changes_within_group_2 = round(total_2_part / total_2_all, 4) * 100
        final_changes = ((changes_within_group_1 * 100) - (changes_within_group_2 * 100))
        result = '{0:.2f}'.format(final_changes)
        print(
            f'Разница в группе {age_group} составляет {result} %. В {year1} процентное соотношение было {changes_within_group_1}%, а в {year2} стало {changes_within_group_2}% ')


find_mothers_age_diff(2005, 2006, '25–29')
