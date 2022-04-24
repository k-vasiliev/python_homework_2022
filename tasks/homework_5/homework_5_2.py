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
    with open(r'data\births-by-mothers-age.csv', 'r', encoding='utf8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            if (row['Period'] == str(year1)) and (row['Mothers_Age'] == 'Total'):
                total_count_by_first_year = (int(row['Count']))
            if (row['Period'] == str(year2)) and (row['Mothers_Age'] == 'Total'):
                total_count_by_second_year = (int(row['Count']))
            if (row['Period'] == str(year1)) and (row['Mothers_Age'] == age_group):
                age_group_count_by_first_year = (int(row['Count']))
            if (row['Period'] == str(year2)) and (row['Mothers_Age'] == age_group):
                age_group_count_by_second_year = (int(row['Count']))

        ratio_by_first_year = round(age_group_count_by_first_year / total_count_by_first_year * 100, 2)
        ratio_by_second_year = round(age_group_count_by_second_year / total_count_by_second_year * 100, 2)
        delta = abs(round(ratio_by_first_year - ratio_by_second_year, 2))

    print(f'Разница в группе {age_group} составляет {delta}%. В {year1} процентное соотношение было '
          f'{ratio_by_first_year}%, а в {year2} стало {ratio_by_second_year}%')


find_mothers_age_diff(2006, 2018, '25–29')
