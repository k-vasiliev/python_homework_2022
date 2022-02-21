# Пользователь вводит слово
# Распечатайте является ли введенное слово палиндромом (True/False)
user_input = input("Введите слово: ")

#не будем учитывать регистр букв, т.к. это не является условием для палиндрома
is_palindrome = user_input.lower() == user_input[::-1].lower()

print(is_palindrome)