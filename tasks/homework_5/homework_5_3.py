"""
В html странице data/oscar.html таблица с мужчинами, получившими оскар
Распарсите ее значения и сохраните в csv файл с названием 'man_oscars.csv'
"""

import bs4
import os
import pandas as pd

with open('/Users/nikaborisova/PycharmProjects/python_homework_2022/tasks/homework_5/data/oscar.html') as html_file:
    parser = bs4.BeautifulSoup(html_file.read(), features="html.parser")

    header = parser.findAll('tr')[0]
    header_list = []
    for item in header.findAll('td'):
        header_list.append(item.text.strip())

    row = parser.findAll('tr')[1:]
    row_year_list = []
    row_age_list = []
    row_name_list = []
    row_movie_list = []
    for item in row:
        row_year_list.append(item.findAll('td')[0].text.strip())
        row_age_list.append(item.findAll('td')[1].text.strip())
        row_name_list.append(item.findAll('td')[2].text.strip())
        row_movie_list.append(item.findAll('td')[3].text.strip())

os.chdir('/Users/nikaborisova/PycharmProjects/python_homework_2022/tasks/homework_5/data')
data_frame = pd.DataFrame(data = zip(row_year_list, row_age_list, row_name_list, row_movie_list), columns = header_list)
data_frame.to_csv('man_oscars.csv')
