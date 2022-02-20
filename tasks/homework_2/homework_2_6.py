# Пользователь вводит слово
# Распечатайте является ли введенное слово палиндромом (True/False)

n = input()


if n == n[:: -1]:
    print(True)
else:
    print(False)
