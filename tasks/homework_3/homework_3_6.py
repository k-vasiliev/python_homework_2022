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

i = 1
x = []
while i <= N:
    x.append(i)
    i = i + 1
    print(x)
