# Пользователь вводит слово
# Распечатайте является ли введенное слово палиндромом (True/False)
user_input = input()
# разворачиваем строку
inverse_string = user_input[::-1]
# сравниваем прямую и перевернутую строки. Для палиндрома они должны совпадать
print(user_input == inverse_string)
