# пользователь вводит две строки (по очереди)

# Считайте ввод и распечатайте первую фразу с места, где заканчивается вторая
# пример:
# пользователь ввел "Hello, welcome"
# пользователь ввел "Hello"
# вывод ", welcome"

input1 = input()
input2 = input()

#ищем вхождение второй строки в первую

if input1.find(input2) != -1:
    start_position = input1.find(input2)
    end_position = len(input2)
    print(input1[start_position + end_position:])
else:
    print('Второй строки нет в первой, обрезать не сможем')