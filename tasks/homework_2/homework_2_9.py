# Наименьший делитель
# Пользователь вводит целое число, не меньшее 2
# Выведите его наименьший натуральный делитель, отличный от 1

user_input = int(input())
i = 1
while i <= user_input:
 i = i + 1
 if user_input % i == 0:
    print(i)
    break
