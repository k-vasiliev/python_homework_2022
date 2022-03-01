# Наименьший делитель
# Пользователь вводит целое число, не меньшее 2
# Выведите его наименьший натуральный делитель, отличный от 1

user_input = int(input())
denominator = 2
while user_input % denominator != 0:
    denominator += 1
print (denominator)