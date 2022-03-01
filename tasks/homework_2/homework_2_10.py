"""
Группа из 3 студентов пишет заявки на желаемые факультативы из списка: английский, немецкий, право, математика, сольфеджио. Факультатив откроют, если на него запишутся все студенты.
 Каждый студент может выбрать минимум один и максимум три факультатива. Нужно посчитать количество факультативов, которые откроются.

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

student_1_disciplines = input()
student_2_disciplines = input()
student_3_disciplines = input()

set1 = set(student_1_disciplines.split(' '))
set2 = set(student_2_disciplines.split(' '))
set3 = set(student_3_disciplines.split(' '))

intersect = set1 & set2 & set3

if intersect == set():
    print('0 courses')
else:
    print(len(intersect), ' courses')


