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
    year1 = str(year1)
    year2 = str(year2)
    with open("data/births-by-mothers-age.csv", encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        # идём по строкам и выполняем проверки
        for row in reader:
            if row['Mothers_Age'] == age_group:
                if row['Period'] == year1:
                    count1 = int(row['Count'])
                if row['Period'] == year2:
                    count2 = int(row['Count'])
            elif row['Mothers_Age'] == 'Total':
                if row['Period'] == year1:
                    total1 = int(row['Count'])
                if row['Period'] == year2:
                    total2 = int(row['Count'])
    # считаем % и их разницу
    percent1 = round(count1 / total1 * 100, 2)
    percent2 = round(count2 / total2 * 100, 2)
    percent_diff = round(percent2 - percent1, 2)
    print(f'Разница в группе {age_group} составляет {percent_diff}%. \n'
          f'В {year1} процентное соотношение было {percent1}%, а в {year2} стало {percent2}%')


find_mothers_age_diff(2015, 2016, '25–29')
