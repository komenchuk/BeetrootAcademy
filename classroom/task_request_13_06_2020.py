"""
Напишем простой парсер новостей. В качестве источника будем использовать сайт Habr.com
Помимо библиотеки requests нам также понадобится билиотека BeatifulSoup
(это библиотека Python для извлечения данных из файлов HTML и XML).
"""

import requests
from bs4 import BeautifulSoup


class HabrPythonNews:

    def __init__(self):
        self.url = 'https://habr.com/ru/hub/python/'
        self.html = self.get_html()

    # Метод get_html() класса DouPythonNews с помощью библиотеки Requests отправляет наш запрос GET к сайту
    # Habr.com и возвращает содержимое страницы в виде текста.
    def get_html(self):
        try:
            result = requests.get(self.url)
            result.raise_for_status()
            return result.text
        except(requests.RequestException, ValueError):
            print('Server error')
            return False

    def get_python_news(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        news_list = soup.findAll('h2', class_='post__title')
        return news_list


if __name__ == "__main__":
    news = HabrPythonNews()
    print(news.get_python_news())
