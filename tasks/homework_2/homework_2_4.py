# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой

user_input = input()
# Разбиваем в список
string_list = user_input.split(" ")
# Превращаем строки в числа
integer_map = map(int, string_list)
integer_list = list(integer_map)
# Преобразуем во множество
input_set = set(integer_list)
if len(input_set) < len(integer_list):
    print(0)
else:
    summ = sum(integer_list)
    print(summ)
