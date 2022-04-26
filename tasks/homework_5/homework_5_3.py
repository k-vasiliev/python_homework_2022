"""
В html странице data/oscar.html таблица с мужчинами, получившими оскар
Распарсите ее значения и сохраните в csv файл с названием 'man_oscarcs.csv'

"""

from bs4 import BeautifulSoup
import csv

list = []
list_csv = []

with open('C://Users//q2364//Desktop//python_homework_2022//tasks//homework_5//data//oscar.html') as html_file:
    parser = BeautifulSoup(html_file.read(), features="html.parser")
    result = parser.find_all('td')
    for element in range(len(result)):
        content = result[element].get_text()
        list.append(content)

for i in range(int(len(list) / 4)):
    list_csv.append(list[0:4])
    del list[0:4]

    with open('data/man_oscars.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar='|')
        writer.writerows(list_csv)
