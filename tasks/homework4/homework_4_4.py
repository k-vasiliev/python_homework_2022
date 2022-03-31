"""
Напишите функцию, которая ищет в тексте слова, начинающиеся на а и на е

"""


import re


def find_words_starts_with_ae(text: str) -> list:
    """
    Принимает текст и возвращает список из слов
    """
    words_list = re.findall(r'\b[aeAE](?:\w+|\s)', example_input)
    return words_list


example_input = "The following example creates an ArrayList with a capacity of 50 elements.\
        Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
print(find_words_starts_with_ae(example_input))
