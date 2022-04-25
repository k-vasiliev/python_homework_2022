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


def find_mothers_age_diff(year1: int, year2: int, age_group: str):
    with open('data/births-by-mothers-age.csv', 'r', encoding='utf8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            if str(year1) == row['Period'] and row['Mothers_Age'] == 'Total':
                total_by_year1 = int(row['Count'])
            if str(year1) == row['Period'] and row['Mothers_Age'] == age_group:
                total_by_age1 = int(row['Count'])
            if str(year2) == row['Period'] and row['Mothers_Age'] == 'Total':
                total_by_year2 = int(row['Count'])
            if str(year2) == row['Period'] and row['Mothers_Age'] == age_group:
                total_by_age2 = int(row['Count'])

    percent1 = round((total_by_age1 * 100) / total_by_year1, 2)
    percent2 = round((total_by_age2 * 100) / total_by_year2, 2)
    if percent2 >= percent1:
        percent_difference = round(percent2 - percent1, 2)
    else:
        percent_difference = round(percent1 - percent2, 2)
    print(
        f'Разница в группе {age_group} составляет {percent_difference}%. В {year1} процентное соотношение было {percent1}%, а в {year2} стало {percent2}%')


find_mothers_age_diff(2005, 2006, '25–29')

