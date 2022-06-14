"""

В математике существует так называемая последовательность чисел Фибоначчи
Выглядит она так: 1, 1, 2, 3, 5, 8, 13, ...

Каждое последующее число равно сумме двух предыдущих,
а первые два числа Фибоначчи - две единицы.

Запросите с клавиатуры число N и распечатайте через запятую первые N чисел Фибоначчи

Ввод: 6
Вывод: 1, 1, 2, 3, 5, 8

"""

User_input = int(input())
first_two_fibonacci_numbers = [1, 1]
for i in range(1, User_input-1):
    fibonacci_number = int(first_two_fibonacci_numbers[-2]) + int(first_two_fibonacci_numbers[-1])
    first_two_fibonacci_numbers.append(fibonacci_number)
print(*first_two_fibonacci_numbers, sep = ', ')
