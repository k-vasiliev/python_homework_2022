# Пользователь вводит слово
# Распечатайте является ли введенное слово палиндромом (True/False)

user_input = input()
rev_input = (user_input[::-1])

print(rev_input == user_input)