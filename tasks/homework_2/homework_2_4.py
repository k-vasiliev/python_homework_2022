# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой

user_input = input()

print(user_input)

x1 = int(user_input[:user_input.find(' ')])
user_input2 = user_input[user_input.find(' ') + 1:]
x2 = int(user_input2[:user_input2.find(' ')])
x3 = int(user_input2[user_input2.find(' ') + 1:])

if x1 == x2 or x1 == x3 or x2 == x3:
    print(int(0))
else:
    print(x1 + x2 + x3)