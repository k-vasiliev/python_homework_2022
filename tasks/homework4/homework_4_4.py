"""
Напишите функцию, которая ищет в тексте слова, начинающиеся на а и на е

"""

import re


def find_words_starts_with_ae(text: str) -> list:
    """
    Принимает текст и возвращает список из слов
    """
    pass  # тут ваше решение
    return re.findall(r"\b[a,e]\w\w*", text)# слова состоящие минимум из 2х букв

example_input = "The following example creates an ArrayList with a capacity of 50 elements.\
        Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
print(find_words_starts_with_ae(example_input))
