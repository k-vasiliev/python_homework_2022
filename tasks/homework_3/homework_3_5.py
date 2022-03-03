"""

В математике существует так называемая последовательность чисел Фибоначчи
Выглядит она так: 1, 1, 2, 3, 5, 8, 13, ...

Каждое последующее число равно сумме двух предыдущих,
а первые два числа Фибоначчи - две единицы.

Запросите с клавиатуры число N и распечатайте через запятую первые N чисел Фибоначчи

Ввод: 6
Вывод: 1, 1, 2, 3, 5, 8

"""

N = int(input())

my_list = [0]

for i in range(N):
    if len(my_list) == 1:
        my_list.append(i+1)
    else:
        x = my_list[i-1] + my_list[i]
        my_list.append(x)

print(', '.join(map(str, my_list[1:])))
#0 тоже относится к последовательности Фибоначчи btw, но вывод имеет другой шаблон