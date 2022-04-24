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


def find_mothers_age_diff(year1: int, year2: int, age_group: str):
    import csv

    file_path = 'data/births-by-mothers-age.csv'
    with open(file_path, newline=(''), encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        # years_counter = 0
        # group_counter = 0
        for row in reader:
            cell_list = row[0].split(';')
            if cell_list[0] == str(year1) and cell_list[1] == '15–19':
                first_w_in_gr = cell_list[2]
            cell_list = row[0].split(';')
            if cell_list[0] == str(year1) and cell_list[1] == age_group:
                first_year_women_in_group = cell_list[2]
            if cell_list[0] == str(year1) and cell_list[1] == 'Total':
                first_year_women_in_total = cell_list[2]
            if cell_list[0] == str(year2) and cell_list[1] == age_group:
                second_year_women_in_group = cell_list[2]
            if cell_list[0] == str(year2) and cell_list[1] == 'Total':
                second_year_women_in_total = cell_list[2]
    # if years_counter == 0 or group_counter == 0:
    #     print('gg')
    # breakpoint()

    first_year_percent = round(int(first_year_women_in_group) / int(first_year_women_in_total) * 100, 2)
    second_year_percent = round(int(second_year_women_in_group) / int(second_year_women_in_total) * 100, 2)
    percent_diff = round(second_year_percent - first_year_percent,2)

    print(f'Разница в группе {age_group} составляет {percent_diff}%. В {year1} процентное соотношение было {first_year_percent}%, а в {year2} стало {second_year_percent}%')


find_mothers_age_diff(2005, 2006, '25–29')
