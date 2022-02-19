# Пользователь вводит слово
# Распечатайте является ли введенное слово палиндромом (True/False)
word = input()
reverse_word = word[::-1]
if word == reverse_word:
    is_palindrom = True
else:
    is_palindrom = False
print(is_palindrom)