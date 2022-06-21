"""

На вход принимается число N.

Выведите на печать следующий паттерн:

1
1 2
1 2 3
1 2 3 4
...
1 ... N

"""

user_input = int(input())
list_of_numbers = []

for i in range(1, user_input+1):
    list_of_numbers.append(i)
    print(' '.join(map(str, list_of_numbers)))
