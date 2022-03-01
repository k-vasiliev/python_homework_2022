# Пользователь вводит слово
user_input = input()
reversed_input = user_input[::-1]
# Распечатайте является ли введенное слово палиндромом (True/False)
if user_input == reversed_input:
    print(True)
else:
    print(False)