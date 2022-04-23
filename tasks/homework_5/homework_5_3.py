"""
В html странице data/oscar.html таблица с мужчинами, получившими оскар
Распарсите ее значения и сохраните в csv файл с названием 'man_oscarcs.csv'

"""
from bs4 import BeautifulSoup as bs #где-то читал, что элиасы для библиотек зло, но камон, компактность же, аналитикам же норм называть таблицы as tbl_345 и черт пойми что там лежит) сам так делаю, а я тимлид, бедные мои джуны(
import os

#сменим директорию
os.chdir('C:\\Users\\79031\\PycharmProjects\\python_homework_2022\\tasks\\homework_5\\data')

#спляшем с бубном
with open('man_oscars.csv', 'w', encoding='utf-8') as man_oscars_csv:
    with open('oscar.html') as web_page:
        #распарсим все до строк
        parsed_page = bs(web_page.read(), features='html.parser')
        tables = parsed_page.find_all('table') #т.к. в файле одна таблица, то найдем эту одну таблицу
        table_rows = tables[0].find_all('tr')
        #пойдем парсить строки
        for row in table_rows:
            row_2_insert = '' #пустая текстовая строка
            for element in row.find_all('td'):
                row_2_insert = row_2_insert + str(element.text.strip()) + ',' #присобачим все в строку, в конце будет лишняя запятая
            man_oscars_csv.write(f'{row_2_insert.strip(",")}\n')