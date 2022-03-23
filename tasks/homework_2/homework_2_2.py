# пользователь вводит две строки (по очереди)

# Считайте ввод и распечатайте первую фразу с места, где заканчивается вторая
# пример:
# пользователь ввел "Hello, welcome"
# пользователь ввел "Hello"
# вывод ", welcome"

input1 = input()
input2 = input()
# в первом вводе ищем второй ввод
file_format = input1.find(input2)

print(input1[file_format+len(input2):])








