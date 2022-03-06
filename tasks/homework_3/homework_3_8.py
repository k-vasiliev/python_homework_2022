"""

Пользователь вводит число
Посчитайте общее количество цифр и уникальных. Выведите через запятую без пробела

Вход: 922383
Выход: 6,4

"""

number = int(input())
result = []
while number > 0:
    result.append(number % 10)
    number //= 10
result.reverse()
user_list = []
count = 0
for i in result:
    if i not in user_list:
        count = count + 1
    user_list.append(i)
print(str(len(result))+',', count)
