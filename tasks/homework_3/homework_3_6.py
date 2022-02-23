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

N = int(input())
for i in range(1, N + 1):
    for j in range(1, i + 1):
        print(j, end = ' ')
    print("")
