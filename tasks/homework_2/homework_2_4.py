# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой

user_input = input()
split_set = user_input.split(" ")

split_set = user_input.split(" ")

if int(split_set[0]) == int(split_set[1]) or int(split_set[0]) == int(split_set[2]) or int(split_set[1]) == int(split_set[2]):
    print(0)
else:
    print(int(split_set[0]) + int(split_set[1]) + int(split_set[2]))
