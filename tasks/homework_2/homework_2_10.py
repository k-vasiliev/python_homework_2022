# """
# Группа из 3 студентов пишет заявки на желаемые факультативы из списка: английский, немецкий, право, математика,
# сольфеджио. Факультатив откроют, если на него запишутся все студенты. Каждый студент может выбрать минимум один и
# максимум три факультатива. Нужно посчитать количество факультативов, которые откроются.
#
# Пример
#
# Ввод:
#
# английский сольфеджио право
# математика сольфеджио
# немецкий право
#
# Вывод:
#
# 0
#
# Ввод:
#
# математика немецкий право
# математика немецкий
# немецкий право математика
#
# Вывод:
# 2
# """

student_1_disciplines = set(input('Заявка 1: ').lower().split(' '))
student_2_disciplines = set(input('Заявка 2: ').lower().split(' '))
student_3_disciplines = set(input('Заявка 3: ').lower().split(' '))

student_1_2_intersection = student_1_disciplines.intersection(student_2_disciplines)
student_2_3_intersection = student_2_disciplines.intersection(student_3_disciplines)

print(len(student_1_2_intersection.intersection(student_2_3_intersection)))