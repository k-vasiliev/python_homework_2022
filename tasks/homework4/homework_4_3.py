"""
Владимир устроился на работу в одно очень важное место
И в первом же документе он ничего не понял, там были сплошные ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п.
Тогда он решил собрать все аббревиатуры, чтобы потом найти их расшифровки.

Помогите ему написать ему такую функцию.
Будем считать аббревиатурой слова только лишь из заглавных букв (как минимум из двух).
Если несколько таких слов разделены пробелами, то они считаются одной аббревиатурой.


"""

import re


def find_abbreviations(text: str) -> list:
    """
    Принимает текст и возвращает список из аббревиатур
    """
    result = re.findall(r"\b[А-Я]+(?:\s[А-Я]{2,})+|[А-Я]{2,}\b", text)
    return result


example_input = 'Это курс информатики соответствует ФГОС и ПООП, это подтверждено ФГУ ФНЦ НИИСИ РАН'
print(find_abbreviations(example_input))
