"""
В html странице data/oscar.html таблица с мужчинами, получившими оскар
Распарсите ее значения и сохраните в csv файл с названием 'man_oscarcs.csv'

"""
from bs4 import BeautifulSoup
import csv
list_final1 = []
get_csv = []


with open('data/oscar.html') as file:
    soup = BeautifulSoup(file, 'lxml')
    to_find = soup.find_all('td')

for i in range(len(to_find)):
    get_text = to_find[i].get_text()
    list_final1.append(get_text)
    print(list_final1)

for i in range(int(len(list_final1) // 4)):
    titles = list_final1[0:4]
    get_csv.append(titles)
    del list_final1[0:4]
    with open('data/man_oscarcs.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(get_csv)




