# Пользователь вводит слово
# Распечатайте является ли введенное слово палиндромом (True/False)

def palindrome(s):
    return s[::-1] == s
while True:
    s = input("ввести текст: ").lower()
    print(f"{s} - ПАЛИНДРОМ" if palindrome(s) else "не палиндром")
    break