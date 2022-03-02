# Пользователь вводит слово
# Распечатайте является ли введенное слово палиндромом (True/False)
user_input = list(input("Введите слово-палиндром: "))
user_reverse = list(reversed(user_input))
if user_input == user_reverse:
    print("True")
else:
    print("False")
