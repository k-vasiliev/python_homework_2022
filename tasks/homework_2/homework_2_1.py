# пользователь вводит слово. Для простоты будем считать,
# что слово не меньше 3 символов
user_input = input("Введите слово длиной не менее 3 символов: ")
# Считайте ввод и распечатайте:
print(user_input)
# длину слова
print(len(user_input))
# слово без первой буквы
print(user_input[1:])
# последний символ слова
print(user_input[-1])
# слово без последних двух букв
print(user_input[:-2])
# слово в uppercase
print(user_input.upper())