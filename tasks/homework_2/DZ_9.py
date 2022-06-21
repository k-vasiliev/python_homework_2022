# Наименьший делитель
# Пользователь вводит целое число, не меньшее 2
# Выведите его наименьший натуральный делитель, отличный от 1

user_input = int(input("Введите целое число: "))
new_list = []
if user_input >= 2:
    for i in range(2, user_input):
        if (user_input % i == 0):
            new_list.append(i)
#            print(i)
    if min(map(int, new_list)) != 1:
        print("наименьший натуральный делитель", min(map(int, new_list)))
    else:
        print("наименьший натуральный делитель", user_input)

