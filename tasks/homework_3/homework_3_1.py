"""
Пользователь вводит строку с клавиатуры
Найти частоту слов в строке

Вход: "Я не кидал никого никогда"

Выход:

Я:1
не:1
кидал:1
никого:1
никогда:1

"""

user_input = str(input())
user_input = user_input.split(" ")
new_list = []
for i in user_input:
    if i not in new_list:
        new_list.append(i)
        print(new_list)
#print("полный уникальный", new_list)

for i in range(0, len(new_list)):
    count_user_input = user_input.count(new_list[i])
    print(f"{new_list[i]}:{count_user_input}")



