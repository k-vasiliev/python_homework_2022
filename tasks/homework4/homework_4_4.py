"""
Напишите функцию, которая ищет в тексте слова, начинающиеся на а и на е

"""

import re


def find_words_starts_with_ae(text: str) -> list:
    """
    Принимает текст и возвращает список из слов
    """
    return list(dict.fromkeys(re.findall(r"\b[aAeE]\w*", text)))


example_input = "The following example creates an ArrayList with a capacity of 50 elements.\
        Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
print(find_words_starts_with_ae(example_input))
