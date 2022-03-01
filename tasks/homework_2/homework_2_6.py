# Пользователь вводит слово
# Распечатайте является ли введенное слово палиндромом (True/False)
user_input = list(input())
rever_input = list(reversed(user_input))
if user_input == rever_input:
    print('Палиндром')
else:
    print('Nice try, but not')