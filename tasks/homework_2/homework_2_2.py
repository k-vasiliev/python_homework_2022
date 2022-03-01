# пользователь вводит две строки (по очереди)

# Считайте ввод и распечатайте первую фразу с места, где заканчивается вторая
# пример:
# пользователь ввел "Hello, welcome"
# пользователь ввел "Hello"
# вывод ", welcome"

input1 = input()
input2 = input()

len_input2 = len(input2)
find_input2_start = input1.find(input2)

print(input1[input1.find(input2) + len_input2:])
