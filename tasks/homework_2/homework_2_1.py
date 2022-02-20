# пользователь вводит слово. Для простоты будем считать,
# что слово не меньше 3 символов
# Считайте ввод и распечатайте:
some_word = ('bravo')

# длину слова
print(len(some_word))

# слово без первой буквы - ravo
print(some_word[1:])

# последний символ слова - o
print(some_word[4])

# слово без последних двух букв - bra
print(some_word[0:3])

# слово в uppercase - BRAVO
some_word = 'bravo'.upper()
print(some_word)
