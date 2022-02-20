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

student_1_disciplines = 'математика немецкий право'
student_1_disciplines_lst = set(student_1_disciplines.split())
student_2_disciplines = 'математика немецкий'
student_2_disciplines_lst = set(student_2_disciplines.split())
student_3_disciplines = 'немецкий право математика'
student_3_disciplines_lst = set(student_3_disciplines.split())
list_of_subjects = ['английский', 'немецкий', 'право', 'математика', 'сольфеджио']
dict_facultates = {x: 0 for x in list_of_subjects}

result = student_1_disciplines_lst.intersection(student_2_disciplines_lst, student_3_disciplines_lst)

if len(result) == 0:
    print(0)
elif 3 >= len(result) > 0:
    print(len(result))
