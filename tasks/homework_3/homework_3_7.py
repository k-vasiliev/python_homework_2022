"""

Пользователь вводит строку, состоящая из слов

Сделайте из нее аббревиатуру с помощью list comprehension и распечатайте

Вход: "Комитет Государственной Безопасности"
Выход: "КГБ"

"""
#words = input("Вход: ")
#abbr = ''.join(word[0] for word in words.upper().split())
#print("Выход: ", abbr)

print(''.join(word[0] for word in input().upper().split()))