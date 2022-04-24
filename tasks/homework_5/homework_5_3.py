"""
В html странице data/oscar.html таблица с мужчинами, получившими оскар
Распарсите ее значения и сохраните в csv файл с названием 'man_oscarcs.csv'

"""

from bs4 import BeautifulSoup
import csv

data_from_html = []
data_to_csv = []

with open('data/oscar.html', 'r') as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'html.parser')
    rows = soup.find_all('td')
    for row in rows:
        data_to_append = row.get_text()
        data_from_html.append(data_to_append)

for i in range(int(len(data_from_html) / 4)):
    data_to_csv.append(data_from_html[0:4])
    del data_from_html[0:4]

with open('man_oscarcs.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data_to_csv)
