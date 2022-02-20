# пользователь вводит две строки (по очереди)

# Считайте ввод и распечатайте первую фразу с места, где заканчивается вторая
# пример:
# пользователь ввел "Hello, welcome"
# пользователь ввел "Hello"
# вывод ", welcome"

input1 = input()
input2 = input()
my_list = []

result = input1 + " " + input2
find_index = result.rfind(input2)

if input1.find(' ') > 0:
    result = result[-find_index:find_index-1]
else:
    result = input1
print(result)
