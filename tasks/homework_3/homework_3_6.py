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
    x = 1
    while i > 0:
        print(x, end=' ')
        x += 1
        i -= 1
        if i == 0:
            print(end='\n')
