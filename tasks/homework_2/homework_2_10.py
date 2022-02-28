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

student_1_disciplines = input()
student_2_disciplines = input()
student_3_disciplines = input()

student_1_disciplines_set = set(student_1_disciplines.split(" "))
student_2_disciplines_set = set(student_2_disciplines.split(" "))
student_3_disciplines_set = set(student_3_disciplines.split(" "))

student_1_2_inter = student_1_disciplines_set.intersection(student_2_disciplines_set)
student_2_3_inter = student_2_disciplines_set.intersection(student_3_disciplines_set)

print(len(student_1_2_inter.intersection(student_2_3_inter)))