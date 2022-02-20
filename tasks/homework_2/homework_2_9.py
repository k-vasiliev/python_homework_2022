# Наименьший делитель
# Пользователь вводит целое число, не меньшее 2
# Выведите его наименьший натуральный делитель, отличный от 1

user_input = int(input())
z = 2
for z in range(z, user_input+1):
    if user_input % z == 0:
        print(z)
        break
    else:
        z += 1
