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
    with open("./data/births-by-mothers-age.csv", encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            if row['Period'] == str(year1) and row['Mothers_Age'] == age_group:
                count1 = int(row['Count'])
            if row['Period'] == str(year1) and row['Mothers_Age'] == 'Total':
                total1 = int(row['Count'])
                percent1 = round(count1 / total1 * 100, 2)
            if row['Period'] == str(year2) and row['Mothers_Age'] == age_group:
                count2 = int(row['Count'])
            if row['Period'] == str(year2) and row['Mothers_Age'] == 'Total':
                total2 = int(row['Count'])
                percent2 = round(count2 / total2 * 100, 2)
                diff_percent = round((percent2 - percent1),2)
                print(f'Разница в группе {age_group} составляет {diff_percent}%. В {year1} процентное соотношение было {percent1}%, а в {year2} стало {percent2}%')


find_mothers_age_diff(2015, 2016, '25–29')
