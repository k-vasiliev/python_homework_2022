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
    with open('/Users/nikaborisova/PycharmProjects/python_homework_2022/tasks/homework_5/data/births-by-mothers-age.csv') as stats:
        reader = csv.DictReader(stats, delimiter = ';')
        for row in reader:
            if row['Mothers_Age'] == age_group:
                if int(row['Period']) == year1:
                    count_year1 = int(row['Count'])
                elif int(row['Period']) == year2:
                    count_year2 = int(row['Count'])
            if row['Mothers_Age'] == 'Total':
                if int(row['Period']) == year1:
                    total_year1 = int(row['Count'])
                elif int(row['Period']) == year2:
                    total_year2 = int(row['Count'])
        perc1 = count_year1/total_year1*100
        perc2 = count_year2/total_year2*100
        diff = abs(perc2 - perc1)
        print(f'Разница в группе {age_group} составляет {round(diff, 2)}%. В {year1} процентное соотношение было {round(perc1, 2)}%, а в {year2} стало {round(perc2, 2)}%')
    return
find_mothers_age_diff(2005, 2006, '25–29')