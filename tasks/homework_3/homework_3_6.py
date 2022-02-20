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

for i in range(0, N):
    for j in range(0, i+1):
        print(j+1, end=' ')
    print()
