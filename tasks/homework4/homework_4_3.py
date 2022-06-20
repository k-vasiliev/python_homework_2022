"""
Владимир устроился на работу в одно очень важное место
И в первом же документе он ничего не понял, там были сплошные ФГУП НИЦ ГИДГЕО, ФГОУ ЧШУ АПК и т.п.
Тогда он решил собрать все аббревиатуры, чтобы потом найти их расшифровки.

Помогите ему написать  такую функцию.
Будем считать аббревиатурой слова только лишь из заглавных букв (как минимум из двух).
Если несколько таких слов разделены пробелами, то они считаются одной аббревиатурой.


"""

import re


def find_abbreviations(text: str) -> list:
    """
    Принимает текст и возвращает список из аббревиатур
    """
    #for i in range(len(text)):
            #print(text[i])
    #        if text[i].isupper() == True or text[i+2].isupper() == True or text[i] in ['.', ',', '!', ' ']:
    #            print(text[i])
    #pass
    for bykvi in text.split('\n'):
        bykvi= bykvi.split(' ')
        bykvi = ''.join(bykvi)
        rezult = re.findall(r'([A-ZА-Я]{2,})', bykvi)
        rezult = ', '.join(map(str, rezult))
        #print(rezult)
    return rezult




example_input = 'Это курс информатики соответствует ФГОС и ПООП, это подтверждено ФГУ ФНЦ НИИСИ РАН'
print(find_abbreviations(example_input))
