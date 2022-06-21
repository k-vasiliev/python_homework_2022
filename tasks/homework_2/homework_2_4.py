# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой


user_input = input().split(' ')

int_input = list(map(int, user_input))

summa = int()

#for i in int_input:
#    summa += i

summa = sum(int_input)

for i in range(len(int_input) - 1):
    for j in range(i+1, len(int_input)):
        if int_input[i] == int_input[j]:
            print("Есть одинаковые числа, сумма = 0")
            quit()
else:
    print(summa)
