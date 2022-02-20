# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой

user_input = input()
without_space = user_input.replace(' ', '')
num1, num2, num3 = without_space[0], without_space[1], without_space[2]
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)

if num1 == num2 or num1 == num3 or num2 == num3:
    print(0)
else:
    print(num1 + num3 + num2)
