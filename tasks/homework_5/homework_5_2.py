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
def find_mothers_age_diff (year1: int, year2: int, age_group: str):

    with open(r'C:\Users\julia\Documents\Питон_ВШЭ\births-by-mothers-age.csv') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            if row['Period'] == str(year1) and row['Mothers_Age'] == str(age_group):
                count_year1 = int(row['Count'])
            elif row['Period'] == str(year1) and row['Mothers_Age'] == str('Total'):
                total_year1 = int(row['Count'])
            elif row['Period'] == str(year2) and row['Mothers_Age'] == str(age_group):
                count_year2 = int(row['Count'])
            elif row['Period'] == str(year2) and row['Mothers_Age'] == str('Total'):
                total_year2 = int(row['Count'])
            else:
                print ('такой информации нет')
                break

        percent_year1 = round((count_year1 / total_year1) * 100, 2)
        percent_year2 = round((count_year2 / total_year2) * 100, 2)
        difference = abs(percent_year1 - percent_year2)

    return print(f'Разница в группе {age_group} составляет {difference}%. В {year1} процентное соотношение было {percent_year1}%, а в {year2} стало {percent_year2}%')

find_mothers_age_diff(2005, 2006, '25–29')

