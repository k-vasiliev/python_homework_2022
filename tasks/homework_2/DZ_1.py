# Задание 1
# Считайте ввод и распечатайте:
user_input = str(input())
print(user_input)
# длину слова
n = len(user_input)
result = user_input[1:]

# слово без первой буквы
print("слово без первой буквы: ", result)

# последний символ слова
result2 = user_input[-1]
print("последний символ слова: ", result2)

# слово без последних двух букв
result3 = user_input[:-2]
print("слово без последних двух букв: ", result3)

# слово в uppercase
print("слово в uppercase: ", user_input.upper())