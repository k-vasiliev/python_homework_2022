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
num_elements = 0
my_list = []
for i in range(1, N + 1):
    for k in range(i + 1):
        if k != 0:
            my_list.append(k)
    print(*my_list[0:i])
    del my_list[0:i]
