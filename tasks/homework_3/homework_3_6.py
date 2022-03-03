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

my_list = []

for i in range(1, N+1):
    my_list.append(i)
    print(' '.join(map(str, my_list)))