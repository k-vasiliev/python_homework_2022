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

start = re.search(r'I.', text).end()
# Индекс конца первой главы
end = re.search(r'And Afanasy Ivanovitch heaved a deep sigh.', text).start()


# ваше решение

first_character = text[start:end]

find_the = re.findall("\\b[Tt]he\\b", first_character)

print(len(find_the))