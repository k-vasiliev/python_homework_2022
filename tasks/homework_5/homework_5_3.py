"""
В html странице data/oscar.html таблица с мужчинами, получившими оскар
Распарсите ее значения и сохраните в csv файл с названием 'man_oscars.csv'

"""

from bs4 import BeautifulSoup
import csv

with open("data/oscar.html", "r") as input_file:
    # считываем файл
    contents = input_file.read()

# Делаем суп и парсим строки таблицы по тэгу <tr>
soup = BeautifulSoup(contents, 'lxml')
rows = soup.find_all("tr")

# сохраням результат в csv
with open("man_oscars.csv", "wt+", newline="") as output_file:
    # создаем файл
    writer = csv.writer(output_file)
    # идём по строкам html
    for row in rows:
        csv_row = []
        # находим в каждой строке html ячейки по тэгу <td> и добавляем в строку csv
        for cell in row.find_all(["td"]):
            csv_row.append(cell.get_text())
        # записываем строку csv
        writer.writerow(csv_row)
