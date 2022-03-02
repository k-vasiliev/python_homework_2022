# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой

user_input = input()
find_first_whitespace = user_input.find(' ')
number_1 = float(user_input[:find_first_whitespace])
remaining_data = user_input[find_first_whitespace+1:]

find_second_whitespace = remaining_data.find(' ')
number_2 = float(remaining_data[:find_second_whitespace])
number_3 = float(remaining_data[find_second_whitespace+1:])

if number_1 == number_2 or number_2 == number_3 or number_3 == number_1:
    sum_of_numbers = 0
else:
    sum_of_numbers = number_1 + number_2 + number_3

print(sum_of_numbers)
