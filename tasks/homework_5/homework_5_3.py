"""
В html странице data/oscar.html таблица с мужчинами, получившими оскар
Распарсите ее значения и сохраните в csv файл с названием 'man_oscarcs.csv'

"""

from bs4 import BeautifulSoup
import csv

with open("./data/oscar.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, "html.parser")
    rows = soup.find_all("tr")

with open("man_oscarcs.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for row in rows:
        csv_row = []
        for cell in row.findAll(["td", "th"]):
            csv_row.append(cell.get_text())
        writer.writerow(csv_row)



