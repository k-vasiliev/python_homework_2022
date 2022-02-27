# пользователь вводит три числа через пробел
user_input = input('Необходимо ввести три числа через пробел: ')
# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой
number1, number2, number3 = list(map(int,user_input.split()))
if number1 == number2 or number1 == number3 or number2 == number3:
    print('Ответ 0, т.к. есть числа, которые равны друг другу')
else:
    print(number1 + number2 + number3)
