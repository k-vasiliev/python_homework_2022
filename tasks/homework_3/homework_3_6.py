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

for x in range(1, N + 1):
    for y in range(1, x + 1):
        print(y, end=" ")
    print()
