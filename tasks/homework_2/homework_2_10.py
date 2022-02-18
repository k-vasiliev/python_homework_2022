"""
Группа из 3 студентов пишет заявки на желаемые факультативы из списка: английский, немецкий, право, математика,
сольфеджио.
Факультатив откроют, если на него запишутся все студенты.
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

student_1_disciplines = input()
student_2_disciplines = input()
student_3_disciplines = input()
# переводим во множества
student_1_disciplines = set(student_1_disciplines.split(' '))
student_2_disciplines = set(student_2_disciplines.split(' '))
student_3_disciplines = set(student_3_disciplines.split(' '))

# определяем пересечения множеств
temp = student_1_disciplines.intersection(student_2_disciplines)
temp = temp.intersection(student_3_disciplines)

# результат - длина множества от пересечения
print(len(temp))
