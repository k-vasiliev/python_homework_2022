"""
Найти все числа от 1000 до 3000 включительно, все цифры которых четные.
Программа должна выдавать результат в виде разделенной запятыми строки

"""
# зададим множество четных цифр
even_digits = {0, 2, 4, 6, 8}
# создадим пустой список для чисел, удовлетволяющих условию
all_even = []
# каждое число разделяем на цифры и создаем из них множество. Если оно входит в множество четных цифр, то добавляем число к итоговому списку
for n in range(1000, 3001):
    n_set = {int(a) for a in str(n)}
    if n_set <= even_digits:
        all_even.append(n)

print(*all_even, sep = ", ")
