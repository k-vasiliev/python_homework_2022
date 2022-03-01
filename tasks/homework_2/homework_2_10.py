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
# list = ["английский", "немецкий", "право", "математика", "сольфеджио"]

student_1_disciplines = input()
student_2_disciplines = input()
student_3_disciplines = input()

student_disciplines = list(set(student_1_disciplines.split()) & set(student_2_disciplines.split()) & set(student_3_disciplines.split()))
student_disciplines_sorted = sorted(student_disciplines, key = lambda k : student_1_disciplines.index(k))

if len(student_disciplines_sorted) > 0:
    print(len(student_disciplines_sorted))
else:
    print(0)


