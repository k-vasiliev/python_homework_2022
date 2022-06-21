"""
Пользователь вводит строку. Найдите количество цифр и количество букв в строке
Вход: "абвгд 234"

Выход:

Цифры: 3
Буквы: 5

"""
import re
user_input = input()
number_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
count_numbers = 0
count_letters = 0
count_letters_1 = 0
count = 0

for i in user_input:
    if i in number_list:
        count_numbers = count_numbers + 1
    elif i != " ":
        count_letters_1 = re.findall(r"[a-zA-Z]|[а-яА-ЯёЁ]", user_input)
        count_letters = count_letters + 1
    else:
        count = count+1
print(f"Цифры: {count_numbers}")
print(f"Буквы: {count_letters}")
print(f"Символы: {count}")




