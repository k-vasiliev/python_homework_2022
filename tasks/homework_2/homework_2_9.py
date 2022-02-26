# Наименьший делитель
# Пользователь вводит целое число, не меньшее 2
# Выведите его наименьший натуральный делитель, отличный от 1

user_input = int(input())
for i in range(2, user_input+1):
    if int(user_input) % i == 0:
        print(i)
        break





