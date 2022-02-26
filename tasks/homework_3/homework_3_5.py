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
a = 0
b = 1
suma = 0
list_of_result = []
for i in range(1, N):
    suma = a + b
    a = b
    b = suma
    list_of_result.append(suma)

list_of_result_final = [1] + list_of_result
x = list(map(str, list_of_result_final))

if N == 1:
    print(1)
else:
    print(', '.join(x))
