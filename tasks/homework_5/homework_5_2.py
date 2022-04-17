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

# вариант решения 1
def find_mothers_age_diff(year1: int, year2: int, age_group: str):

    import os
    import csv

    # сменим
    os.chdir('C:\\Users\\79031\\PycharmProjects\\python_homework_2022\\tasks\\homework_5\\data\\')

    # создадим пустой словарь
    csv_data_dict = {}

    # отправим все в словарь, на случай если нам понабится в дальнейшем трогать эти значения вне задачи
    with open('births-by-mothers-age.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.DictReader(csvfile, delimiter=';')
        for row in csv_data:
            if row['Period'] in csv_data_dict.keys():
                period_dict = csv_data_dict.pop(row['Period'])
                period_dict.update({row['Mothers_Age']: row['Count']})
                csv_data_dict.update({row['Period']: period_dict})
            else:
                csv_data_dict.update({row['Period']: {row['Mothers_Age']: row['Count']}})

        # вытаскиваем значения и проихводим расчеты
        year1_dict = csv_data_dict[str(year1)]
        year1_value = year1_dict[age_group]
        year1_total = year1_dict['Total']

        year2_dict = csv_data_dict[str(year2)]
        year2_value = year2_dict[age_group]
        year2_total = year2_dict['Total']

    return print(f'Разница в группе {age_group} составляет {}%. В {year1} процентное соотношение было {}%, а в {year2} стало {}%')

find_mothers_age_diff(2005, 2006, '25–29')

