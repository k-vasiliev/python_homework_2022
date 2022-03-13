"""
Пользователь вводит строку, состоящую из чисел, разделенных пробелом
Используя циклы, найдите наибольшее и наименьшее число в этом списке
Не используйте стандартные функции min и max!
Вход: 10 8 3 15
Выход:
Наибольшее число: 15
Наименьшее число: 3
"""
#user_input = input('Вход: ')          # НЕ ПОНЯТНО КАК РЕШИТЬ ЧЕРЕЗ input, поясните!
list = [10, 8, 3, 15]                 # Ниже есть решение через min max с вытаскиванием списка через map, здесь такое не прокатило!
max = list[0] if list else None
for i in list:
    if i > max:
        max = i
print("Наибольшее число:", max)

min = list[0] if list else None
for i in list:
    if i < min:
        min = i
print("Наименьшее число:", min)

"""
user_input = map(int, input('Ввод: ').split())  # Решение через max и min
list = sorted(user_input)
max = list.pop()
print(max)
min = list[0]
print(min)
"""