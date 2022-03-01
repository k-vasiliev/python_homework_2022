# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой

user_input = input().split()
user_input_list = list(map(int, user_input))
unique_user_input = set(user_input_list)

if len(unique_user_input) < 3:
    sum_num = 0
else:
    sum_num = sum(unique_user_input)
print(sum_num)
