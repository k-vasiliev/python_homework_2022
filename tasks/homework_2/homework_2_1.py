# пользователь вводит слово. Для простоты будем считать,
# что слово не меньше 3 символов

# Считайте ввод и распечатайте:

# написали некоторое решение

# длину слова
# слово без первой буквы
# последний символ слова
# слово без последних двух букв
# слово в uppercase

some_word = input()

print(len(some_word))
print(some_word[1:])
print(some_word[-1])
print(some_word[:-2])
print(some_word.upper())
