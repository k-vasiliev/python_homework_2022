# пользователь вводит слово. Для простоты будем считать,
# что слово не меньше 3 символов

# Считайте ввод и распечатайте:
user_input = input()
print(user_input)
# написали некоторое решение

# длину слова
print(len(user_input))
# слово без первой буквы
print(user_input[1:])
# последний символ слова
print(user_input[:-1])
# слово без последних двух букв
print(user_input[:-2])
# слово в uppercase
print(user_input.upper())
