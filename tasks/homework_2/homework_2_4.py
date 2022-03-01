# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой

user_input = input()
a = user_input.find(' ')
number1 = float(user_input[:a])
rest = user_input[a+1:]

b = rest.find(' ')
number2 = float(rest[:b])
number3 = float(rest[b+1:])

if number1 == number2 or number2 == number3 or number3 == number1:
    sum = 0
else:
    sum = number1 + number2 + number3
print(sum)