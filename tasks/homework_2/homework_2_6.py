# Пользователь вводит слово
word = input('Ввести слово: ').lower()
# Распечатайте является ли введенное слово палиндромом (True/False)
if str(word) == str(word)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")