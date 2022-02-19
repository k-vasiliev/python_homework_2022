# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой

print('Введите три числа через пробел')
user_input = input().split(' ')
user_input_num = list(map(int, user_input))
user_input_set = set(user_input_num)

if len(user_input_set) < 3:
    sum_num = 0
else:
    sum_num = sum(user_input_set)

print(sum_num)
