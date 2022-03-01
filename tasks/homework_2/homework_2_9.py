# Наименьший делитель
# Пользователь вводит целое число, не меньшее 2
# Выведите его наименьший натуральный делитель, отличный от 1
number = int(input('Ввести целое число больше 2: '))
if number < 2:
    print('Ваше число меньше 2')
else:
    divider = 2
    for divider in range(divider, number + 1):
        if number % divider == 0:
            print(divider)
            break
        else:
            divider += 1