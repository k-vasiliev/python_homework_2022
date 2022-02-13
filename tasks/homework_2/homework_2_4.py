# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой

user_input = input()
user_list = user_input.split()
# sum_list = int(user_list[0]) + int(user_list[1]) + int(user_list[2])
if (int(user_list[0]) == int(user_list[1])) or (int(user_list[0]) == int(user_list[2])) \
        or (int(user_list[1]) == int(user_list[2])):
    print(0)
else:
    sum_list = int(user_list[0]) + int(user_list[1]) + int(user_list[2])
    print(sum_list)