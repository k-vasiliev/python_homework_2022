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

number1 = 1
number2 = 1

fib_list = [number1]

for i in range(2, N + 1):
    number2, number1 = number1, number2 + number1
    fib_list.append(number2)

fib_list_to_str_items = list(map(str, fib_list))

print(', '.join(fib_list_to_str_items))
