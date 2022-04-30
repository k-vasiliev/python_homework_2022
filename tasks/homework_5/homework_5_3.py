"""
В html странице data/oscar.html таблица с мужчинами, получившими оскар
Распарсите ее значения и сохраните в csv файл с названием 'man_oscarcs.csv'
"""
from bs4 import BeautifulSoup
import csv
user_list = []
with open('data/oscar.html') as file_html:
    soup = BeautifulSoup(file_html, 'html.parser')
    search = soup.find_all('td')
    for element in range(len(search)):
        text_to_write = search[element].get_text()
        user_list.append(text_to_write)
list_csv = []
for i in range(int(len(user_list) / 4)):
    list_csv.append(user_list[0:4])
    del user_list[0:4]
    with open('data/man_oscarcs.csv', 'w', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerows(list_csv)