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

list_new = [1]
if len(list_new) < N:
    while len(list_new) < N:
        extra = list_new[-1] + 1
        list_new.append(extra)
else:
    list_new = [1]

print(*list_new, sep = " ")
