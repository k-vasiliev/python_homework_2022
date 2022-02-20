# пользователь вводит две строки (по очереди)

# Считайте ввод и распечатайте первую фразу с места, где заканчивается вторая
# пример:
# пользователь ввел "Hello, welcome"
# пользователь ввел "Hello"
# вывод ", welcome"


input1 = input()
first_string ='Hello, welcome'
input2 = input()
second_string = 'Hello'
new_string = 'Hello, welcome'.replace('Hello', ' ')
print(new_string)