"""
По ссылке нам доступен перевод книги Идиот
Вытащим оттуда текст первой главы,
после чего ваша задача посчитать количество вхождений слова the

Заметьте, что the может быть частью слова! Надо достать именно слово the
"""
import re
import urllib.request
from utils import disable_ssl_check

disable_ssl_check()
the_idiot_url = 'https://www.gutenberg.org/files/2638/2638-0.txt'
response = urllib.request.urlopen(the_idiot_url)
text = response.read().decode('utf-8')

start = re.search(r'\**\* START OF THE PROJECT GUTENBERG EBOOK THE IDIOT \**\*', text).end()
# Индекс конца первой главы
end = re.search(r'II\.', text).start()

chapter_1 = text[start:end]
the_list = re.findall(r'\b[Tt]he\b', chapter_1)
count_the = len(the_list)

print(count_the)


