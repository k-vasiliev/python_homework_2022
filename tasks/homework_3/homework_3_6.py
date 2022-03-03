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

n = 0
counter = 0
all_number = list()

while counter < N:
    n += 1
    all_number.append(n)
    print(' '.join(map(str, all_number)))
    counter += 1
