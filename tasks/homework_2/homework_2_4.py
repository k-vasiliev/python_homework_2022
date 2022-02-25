# пользователь вводит три числа через пробел

# Выведите сумму этих чисел. Однако, если хотя бы два из этих чисел равны,
# то сумма будет считаться нулевой

#user_input = input()

"""import math
a, b, c = map(int, input().split())
s = a + b + c
if a != b or a != c or b != c:
    print(0)
else:
    print(sum(s))"""
user_input = input()
print('-'.join(list(map(int,input().split()))))