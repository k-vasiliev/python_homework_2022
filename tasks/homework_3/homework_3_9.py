"""
Пользователь вводит строку, состоящую из чисел, разделенных пробелом
Используя циклы, найдите наибольшее и наименьшее число в этом списке

Не используйте стандартные функции min и max!

Вход: 10 8 3 15
Выход:
Наибольшее число: 15
Наименьшее число: 3
"""

user_input = input()
user_input = user_input.split(" ")
user_input = list(map(int, user_input))
m_max = 0
n_min = 0
for i, value in enumerate(user_input):
    if i == 0:
        m_max = user_input[i]
        n_min = user_input[i]
    else:
        if user_input[i] > m_max:
            m_max = user_input[i]
        if user_input[i] < n_min:
            n_min = user_input[i]

print("Наибольшее число:", m_max)
print("Наименьшее число:", n_min)



