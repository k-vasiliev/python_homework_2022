# пользователь вводит три числа через пробел
user_input = input()

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой
to_list = user_input.split()

digit1 = int(to_list[0])
digit2 = int(to_list[1])
digit3 = int(to_list[2])

if (digit1 == digit2) or (digit1 == digit3) or (digit2 == digit3):
    print('Сумма равна 0')
else:
    print(digit1 + digit2 + digit3)

