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
import os
import csv

year1 = 2005
year2 = 2006
age_group = '25–29'
ttt = []

with open("./data/births-by-mothers-age.csv", encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    #Period, Mothers, Count, *_ = reader.fieldnames
    for row in reader:
        if row['Period'] == year1 and row['Mothers_Age'] == age_group:
           ttt.append(row['Count'])
           print(ttt)
        #if row['Period'] == year2 and row['Mothers_Age'] == age_group:
           # count2 = row['Count']


"""
def find_mothers_age_diff(year1: int, year2: int, age_group: str):
        print(f'Разница в группе {age_group} составляет {}%. В {year1} процентное соотношение было {}%, а в {year2} стало {}%')
"""