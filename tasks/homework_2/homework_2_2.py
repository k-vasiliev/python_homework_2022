# пользователь вводит две строки (по очереди)

# Считайте ввод и распечатайте первую фразу с места, где заканчивается вторая
# пример:
# пользователь ввел "Hello, welcome"
# пользователь ввел "Hello"
# вывод ", welcome"


input1 = input('Введите фразу 1: ')
first_string = input1
input2 = input('Введите фразу 2: ')
second_string = input2
new_string = input1.replace(input2, ' ')
print(new_string)