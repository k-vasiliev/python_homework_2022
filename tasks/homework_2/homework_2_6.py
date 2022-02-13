# Пользователь вводит слово
# Распечатайте является ли введенное слово палиндромом (True/False)
user_line = input()

rev = ''.join(reversed(user_line))
palindrome = user_line == rev
print(palindrome)
