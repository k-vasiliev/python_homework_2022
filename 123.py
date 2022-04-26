"""import requests
from bs4 import BeautifulSoup
url = 'https:en.wikipedia.org/wiki/Special:Random'
page = requests.get(url)
page.encoding = 'utf-8'


soup = BeautifulSoup(page.text)
links = soup.find_all('a', text = True)

for l in links:
    l_link = l.get('href')

    if type(l_link) == str and l.link.startwith('/wiki'): #
        print(l.link)
"""
## XLWINGS and OPENPYXL
"""
from datetime
from openpyxl import Workbook,

workbook = Workbook()
worksheet = workbook.active
worksheet.title = 'Students'
worksheet['A1'] = 'First name'
worksheet['B1'] = 'Second name'
worksheet['C1'] = 'Age'
worksheet['D1'] = 'Registration date'

worksheet['A2'] = 'Maria'
worksheet['B2'] = 'The first'
worksheet['B2'] = 28
worksheet['B2'] = datetime.now()
"""
"""
import sqlite3

connection = sqlite3.connect('library.db')
cursor = connection.cursor()
#authors = cursor.execute('SELECT * FROM author')
#for author in authors:
    #(id, book_name, isbn, author_id) = autor
    #print(id, book_name, isbn, author_id)
connection.close()
# Прочитать LIST
# Удалить DELETE id_книги
"""
import sqlite3

def get_db_cursor():
    connection = sqlite3.connect('library.db')
    cursor = connection.cursor()
    return cursor
def get_all_books():
    cursor = get_db_cursor()
    books = cursor.execute('''
    SELECT * FROM books''')
    return books

