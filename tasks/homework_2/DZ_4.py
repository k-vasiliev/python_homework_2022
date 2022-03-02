# Задание_4
# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой

user_input3 = str(input("введите последовательносиьь "))
user_input3_n = user_input3.split()
user_input3_n = list(user_input3_n)
user_input3_new = list(map(int, user_input3_n))
sum_n = 0
for i in range(len(user_input3_new)):
    if (user_input3_new[0] != user_input3_new[1]) and (user_input3_new[0] != user_input3_new[2]) and (user_input3_new[1] != user_input3_new[2]):
        sum_n = sum_n + user_input3_new[i]
    else:
        sum_n = 0
if sum_n > 0:
    print(sum_n)
else:
    print("нулевая сумма: ", sum_n)

