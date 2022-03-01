"""
Группа из 3 студентов пишет заявки на желаемые факультативы из списка: английский, немецкий, право,
математика, сольфеджио. Факультатив откроют, если на него запишутся все студенты.
Каждый студент может выбрать минимум один и максимум три факультатива.
Нужно посчитать количество факультативов, которые откроются.

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

student_1_disciplines = [input()]
student_2_disciplines = [input()]
student_3_disciplines = [input()]

a = len(student_1_disciplines)
b = len(student_2_disciplines)
c = len(student_3_disciplines)

if 1 < a <= 3:
    x = set(student_1_disciplines) & set(student_2_disciplines) & set(student_3_disciplines)
    print(len(x))

if 1 < b <= 3:
    y = set(student_1_disciplines) & set(student_2_disciplines) & set(student_3_disciplines)
    print(len(y))

if 1 < c <= 3:
    v = set(student_1_disciplines) & set(student_2_disciplines) & set(student_3_disciplines)
    print(len(v))