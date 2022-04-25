import os
import csv


def create_list_from_file(file_in_dir):
    results = []
    with open(file_in_dir, 'r', encoding='utf-8') as f:
        data = csv.DictReader(f)
        for row in data:
            results.append(row)
            print(row)


directory = input('Введите путь к данным: ', )
print('Найдены следующие файлы *.csv:')
for file in os.listdir(directory):
    if file.endswith(".csv"):
        print(os.path.join(file))


create_list_from_file('G:\YandexDisk\РГГРУ\!2021-2022\ПЗ - РМН-18 - весна\Результаты тестов\Тест ПЗ РМН-18 02.03.2022.csv')
