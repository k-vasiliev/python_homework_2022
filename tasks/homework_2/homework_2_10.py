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

# составим список уникальных названий
unique_disc = []
for disc in all_choices:
    if disc in unique_disc:
        continue
    else:
        unique_disc.append(disc)

# составим список: сколько раз сделан выбор каждой дисциплины
disc_count = []
for n in range(len(unique_disc)):
    disc_count.append(all_choices.count(unique_disc[n]))

# для предметов, по которым число выборов равно 3, откроется факультатив
num_facult = []
for elem in disc_count:
    if elem == 3:
        num_facult.append(1)
    else:
        num_facult.append(0)

print(sum(num_facult))

