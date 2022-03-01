# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой

user_input = (input())
a = int(user_input[0])
b = int(user_input[1])
c = int(user_input[2])
total = a + b + c
if a == b or b == c or a == c:
    total = 0
    print(total)
else:
    print(total)