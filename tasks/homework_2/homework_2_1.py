# пользователь вводит слово. Для простоты будем считать,
# что слово не меньше 3 символов
user_word = input()

# Считайте ввод и распечатайте:

# написали некоторое решение

# длину слова
print(len(user_word))

# слово без первой буквы
print(user_word[1:])

# последний символ слова
print(user_word[-1])

# слово без последних двух букв
print(user_word[:-2])

# слово в uppercase
print(user_word.upper())
