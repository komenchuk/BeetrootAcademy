"""
Robots.txt

Download and save to file robots.txt from wikipedia, twitter websites etc.
"""

import requests
from bs4 import BeautifulSoup

html = requests.get(
    "https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D0%BD%D0%B4%D0%B0%D1%80%D1%82_%D0%B8%D1%81%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D0%B9_%D0%B4%D0%BB%D1%8F_%D1%80%D0%BE%D0%B1%D0%BE%D1%82%D0%BE%D0%B2").text
bs4 = BeautifulSoup(html, "html.parser")
tables = bs4.find_all("table")  # получаем список таблиц
for table in tables:
    links = table.find_all("a")  # список всех ссылок
    for link in links:
        try:  # ловим исключение KeyError, ибо атрибут title есть не у всех ссылок
            print(link["title"])  # выводим значение атрибута
        except KeyError:
            pass
