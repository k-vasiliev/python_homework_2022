# Наименьший делитель
# Пользователь вводит целое число, не меньшее 2
# Выведите его наименьший натуральный делитель, отличный от 1

user_input = int(input())
my_list = []

for i in range(1, user_input + 1):
    if i != 1 and user_input % i == 0:
        my_list.append(i)

result = min(my_list)
print(result)
