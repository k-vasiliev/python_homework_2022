"""
Группа из 3 студентов пишет заявки на желаемые факультативы из списка: английский, немецкий,право, математика, сольфеджио. Факультатив откроют, если на него запишутся
все студенты. Каждый студент может выбрать минимум один и максимум три факультатива. Нужно посчитать количество факультативов, которые откроются.

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

student_1_disciplines = 'английский сольфеджио право'
student_2_disciplines = 'математика сольфеджио'
student_3_disciplines = 'немецкий право'
set_student_1_disciplines = set(student_1_disciplines.split())
set_student_2_disciplines = set(student_2_disciplines.split())
set_student_3_disciplines = set(student_3_disciplines.split())

count_disciplines = set_student_1_disciplines.intersection(set_student_2_disciplines, set_student_3_disciplines)
print(len(count_disciplines))


'''
for i in list_student_1_disciplines:
    for a in list_student_2_disciplines:
        for b in list_student_3_disciplines:
            print(i)
'''

