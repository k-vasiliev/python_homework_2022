"""
В html странице data/oscar.html таблица с мужчинами, получившими оскар
Распарсите ее значения и сохраните в csv файл с названием 'man_oscarcs.csv'

"""
import csv

from bs4 import BeautifulSoup

with open(r'data\oscar.html', 'r') as html:
    soup = BeautifulSoup(html.read(), 'html.parser')

rows = soup.find('tbody').findAll('tr')

year = []
age = []
name = []
movie = []

for row in rows:
    year.append(row.findAll('td')[0].text)
    age.append(row.findAll('td')[1].text)
    name.append(row.findAll('td')[2].text)
    movie.append(row.findAll('td')[3].text)

fieldnames = ['year', 'age', 'name', 'movie']

oscar_list_of_dicts = []

for i in range(0, len(rows)):
    oscar_dict = {
        'year': year[i],
        'age': age[i],
        'name': name[i],
        'movie': movie[i]
    }
    oscar_list_of_dicts.append(oscar_dict)

with open('man_oscars.csv', 'w', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(oscar_list_of_dicts)
