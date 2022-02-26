# Пользователь вводит слово
# Распечатайте является ли введенное слово палиндромом (True/False)

word = input()


if word.lower() == word[:: -1].lower():
    print(True)
else:
    print(False)
