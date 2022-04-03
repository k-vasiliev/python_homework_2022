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

# Индекс начала первой главы. Не очень понятно, что считать первой главой? "PART I" или просто "I". Сделал оба условия
# start = re.search(r'\bI\.', text).end()
start = re.search(r'PART\sI\r\n\r', text).end()
# Индекс конца первой главы
# end = re.search(r'\bII\.', text).start()
end = re.search(r'PART\sII\r\n\r', text).start()

# берем текст первой главы
chapter1 = text[start:end]
# ищем вхождения
result = re.findall(r'\b[Tt]he\b', chapter1)
# считаем число
count = len(result)

print(count)
