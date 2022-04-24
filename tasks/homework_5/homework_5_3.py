"""
В html странице data/oscar.html таблица с мужчинами, получившими оскар
Распарсите ее значения и сохраните в csv файл с названием 'man_oscarcs.csv'

"""
from bs4 import BeautifulSoup
import csv

list_of_values = []


def catch_text_from_html():
    with open('data/oscar.html') as file_html:
        soup = BeautifulSoup(file_html, 'html.parser')
        search = soup.find_all('td')
        for element in range(len(search)):
            text_to_write = search[element].get_text()
            list_of_values.append(text_to_write)
    return list_of_values


catch_text_from_html()
list_of_values_to_csv = []


def write_to_csv(list_of_values_from_html):
    for i in range(int(len(list_of_values) / 4)):
        list_of_values_to_csv.append(list_of_values[0:4])
        del list_of_values[0:4]
    with open('data/man_oscarcs.csv', 'w', newline='') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerows(list_of_values_to_csv)
    return file_csv


write_to_csv(list_of_values)
