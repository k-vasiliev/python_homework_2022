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

n = int(input())
new_list = []

for i in range(1, n+1):
    new_list.append(i)
    print(' '.join(map(str, new_list)))


