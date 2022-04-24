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


def find_mothers_age_diff(first_year: int, second_year: int, age_group: str):
    with open(r'data\births-by-mothers-age.csv', 'r', encoding='utf8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            if row['Period'] == str(first_year) and row['Mothers_Age'] == 'Total':
                total_first_year = int(row['Count'])
            if row['Period'] == str(second_year) and row['Mothers_Age'] == 'Total':
                total_second_year = int(row['Count'])
            if row['Period'] == str(first_year) and row['Mothers_Age'] == age_group:
                age_group_first_year = int(row['Count'])
            if row['Period'] == str(second_year) and row['Mothers_Age'] == age_group:
                age_group_second_year = int(row['Count'])

        first_year_value = round(age_group_first_year / total_first_year * 100, 2)
        second_year_value = round(age_group_second_year / total_second_year * 100, 2)
        delta = round(first_year_value - second_year_value, 2)
        print(f'Разница в группе {age_group} составляет {delta}%. В {first_year} процентное соотношение было '
              f'{first_year_value}%, а в {second_year} стало {second_year_value}%')


find_mothers_age_diff(2006, 2005, '25–29')
