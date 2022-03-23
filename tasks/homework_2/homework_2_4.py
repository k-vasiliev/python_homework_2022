# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой

user_input = input()
# Формируем эти числа в список
user_list = user_input.split(' ')
# Переводим список в числа
integer_map = map(int, user_list)
integer_list = list(integer_map)
# Преобразуем в множество
integer_list_set = set(integer_list)
if len(integer_list_set) < len(integer_list):
    print(0)
else:
    summ = sum(integer_list)
    print(summ)
