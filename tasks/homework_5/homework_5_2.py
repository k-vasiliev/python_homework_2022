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

    # отправим все в словарь, т.к. я не хочу решать через if - это скучно
    with open('births-by-mothers-age.csv', 'r', encoding='utf-8') as csvfile:
        csv_data = csv.DictReader(csvfile, delimiter=';')
        for row in csv_data:
            if row['Period'] in csv_data_dict.keys():
                period_dict = csv_data_dict.pop(row['Period'])
                period_dict.update({row['Mothers_Age']: row['Count']})
                csv_data_dict.update({row['Period']: period_dict})
            else:
                csv_data_dict.update({row['Period']: {row['Mothers_Age']: row['Count']}})

        # вытаскиваем значения и производим расчеты
        year1_dict = csv_data_dict[str(year1)]
        year1_value = int(year1_dict[age_group])
        year1_total = int(year1_dict['Total'])

        year2_dict = csv_data_dict[str(year2)]
        year2_value = int(year2_dict[age_group])
        year2_total = int(year2_dict['Total'])

        year_1_result = round((year1_value/year1_total) * 100, 2)
        year_2_result = round((year2_value/year2_total) * 100, 2)
        difference = round(abs(year_2_result - year_1_result), 2)

    return print(f'Разница в группе {age_group} составляет {difference}%. В {year1} процентное соотношение было {year_1_result}%, а в {year2} стало {year_2_result}%')

find_mothers_age_diff(2005, 2006, '25–29')
