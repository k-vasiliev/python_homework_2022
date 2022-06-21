# Наименьший делитель
# Пользователь вводит целое число, не меньшее 2
# Выведите его наименьший натуральный делитель, отличный от 1

user_input = input()
user_input_int = int(user_input)
divider = 2
while user_input_int % divider != 0:
    divider += 1
print(divider)