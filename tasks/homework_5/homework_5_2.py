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
import re
with open('data/births-by-mothers-age.csv', 'r', encoding='utf8') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter = ";")

    for row in csv_reader:
        print(f' Period {row["Period"]} Mothers_Age {row["Mothers_Age"]}', end='')
        print(f' Count {row["Count"]}')

    # Я не понимаю каким образом дальше вытаскивать данные, ничего не получилось.

#def find_mothers_age_diff(year1: int, year2: int, age_group: str):
    #print(f'Разница в группе {age_group} составляет {}%. В {year1} процентное соотношение было {}%, а в {year2} стало {}%')
