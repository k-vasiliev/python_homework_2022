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


# пример 1

student_1_disciplines = ['английский', 'сольфеджио', 'право']
student_2_disciplines = ['математика', 'сольфеджио']
student_3_disciplines = ['немецкий', 'право']



count = int()
for i in student_1_disciplines:
    for j in student_2_disciplines:
        for p in student_3_disciplines:
            if i == j == p:
                count += 1
print(count)

# пример 2

student_1_disciplines = ['математика', 'немецкий', 'право']
student_2_disciplines = ['математика', 'немецкий']
student_3_disciplines = ['немецкий', 'право', 'математика']


count = int()
for i in student_1_disciplines:
    for j in student_2_disciplines:
        for p in student_3_disciplines:
            if i == j == p:
                count += 1
print(count)

