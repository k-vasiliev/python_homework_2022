# Пользователь вводит слово
# Распечатайте является ли введенное слово палиндромом (True/False)

user_input = input()

print(user_input)
a = user_input.lower() == user_input[::-1].lower()
print(a)