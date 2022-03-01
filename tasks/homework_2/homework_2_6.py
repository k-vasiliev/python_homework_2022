# Пользователь вводит слово
# Распечатайте является ли введенное слово палиндромом (True/False)
word = input('Введите слово: ')
word_len = len(word)
for i in range(word_len // 2):
    if word[i] != word[-1-i]:
        print('False')
        quit()
print('True')