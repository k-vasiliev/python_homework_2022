"""
Группа из 3 студентов пишет заявки на желаемые факультативы из списка: английский, немецкий, право, математика, сольфеджио. Факультатив откроют, если на него запишутся все студенты. Каждый студент может выбрать минимум один и максимум три факультатива. Нужно посчитать количество факультативов, которые откроются.

Пример

Ввод:

английский сольфеджио право
математика сольфеджио
немецкий право

Вывод:

0

Ввод:

математика немецкий право
математика немецкий
немецкий право математика

Вывод:
2
"""
student_1_disciplines = input().split(' ')
student_2_disciplines = input().split(' ')
student_3_disciplines = input().split(' ')
all_choices = student_1_disciplines + student_2_disciplines + student_3_disciplines
print (all_choices)
"""
n1 = all_choices.count('английский')
n2 = all_choices.count('немецкий')
n3 = all_choices.count('право')
n4 = all_choices.count('математика')
n5 = all_choices.count('сольфеджио')

num_facult = [0, 0, 0, 0, 0]
for elem in num_facult:

if n1 == 3:
    num_facult[0] = 1
if n2 == 3:
    num_facult[1] = 1
if n3 == 3:
    num_facult[2] = 1
if n4 == 3:
    num_facult[3] = 1
if n5 == 3:
    num_facult[4] = 1
print(sum(num_facult))
"""