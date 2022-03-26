"""
Напишите функцию, которая ищет в тексте слова, начинающиеся на а и на е

"""

import re


def find_words_starts_with_ae(text: str) -> list:
    return re.findall(r'\b[AaEe]\w*', text)

#a, an, are вроде как тоже считаются словами при подсчете объема текста в англ.; решил не использовать lower, чтобы вывести в оригинальном написании

example_input = "The following example creates an ArrayList with a capacity of 50 elements.\
        Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

print(find_words_starts_with_ae(example_input))
