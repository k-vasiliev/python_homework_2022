# Наименьший делитель
# Пользователь вводит целое число, не меньшее 2
# Выведите его наименьший натуральный делитель, отличный от 1

user_input = input().split(' ')

new_input = list(map(int, user_input))

for i in range((new_input[0])):
    if (new_input[0] % (i+2)) == 0:
        print(i+2)
        quit()
