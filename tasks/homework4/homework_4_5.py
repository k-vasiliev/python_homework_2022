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

# start = re.search(r'\*\*\* START OF THIS PROJECT GUTENBERG EBOOK THE IDIOT \*\*\*', raw).end()
"""
Строка выше у меня считывалась с ошибкой AttributeError: 'NoneType' object has no attribute 'end'
Поэтому искал именно начало первой главы 
Так же raw не существует, заменил на text
"""
start = re.search(r'\bPART\sI\r\n\r', text).end()

# Индекс конца первой главы
# end = re.search(r'II', text).start()
# Строкой выше конец первой главы мы не найдем, только указание второй главы в оглавлении, поэтому изменил

end = re.search(r'PART\sII\r\n\r', text).start()

# ваше решение
# вытаскиваем весь текст первой главы
text_of_part_I = text[start:end]

# Ищем The или the где это начало слова и после не идет ни одной буквы
find_all_the = re.findall(r'\b[t|T]he\W', text_of_part_I)

print(len(find_all_the))