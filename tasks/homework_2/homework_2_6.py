# Пользователь вводит слово
users_word = input()

# Распечатайте является ли введенное слово палиндромом (True/False)
users_word_to_list = list(users_word)

palindrome = users_word_to_list == list(reversed(users_word_to_list))

print(palindrome)
