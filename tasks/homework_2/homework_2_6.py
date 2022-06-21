# Пользователь вводит слово
# Распечатайте является ли введенное слово палиндромом (True/False)

user_input = input()

if user_input == user_input[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
