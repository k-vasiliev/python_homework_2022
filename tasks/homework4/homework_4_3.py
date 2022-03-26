"""
Владимир устроился на работу в одно очень важное место
И в первом же документе он ничего не понял, там были сплошные ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п.
Тогда он решил собрать все аббревиатуры, чтобы потом найти их расшифровки.

Помогите ему написать ему такую функцию.
Будем считать аббревиатурой слова только лишь из заглавных букв (как минимум из двух).
Если несколько таких слов разделены пробелами, то они считаются одной аббревиатурой.
"""

import re
"""
#draft

def find_abbreviations(text: str) -> list:
    result_abb_list = []
    for abb in re.findall(r'(?:[A-Я]{2,}\s*)+', text):
        clear_abb = abb.strip()
        result_abb_list.append(clear_abb)
    return result_abb_list
"""
def find_abbreviations(text: str) -> list:
    return re.findall(r'(?:[А-ЯA-Z]{2,}(?:\s[А-ЯA-Z]{2,})+)|[А-ЯA-Z]{2,}', text)

example_input = 'Это курс информатики соответствует ФГОС и ПООП, это подтверждено ФГУ ФНЦ НИИСИ РАН'
print(find_abbreviations(example_input))

