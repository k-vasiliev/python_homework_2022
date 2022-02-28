import statistics
print ('Задание № 5')
CURRENT_YEAR = 2022

student_list = (
     "Иван Питонов", 2001, [8, 7, 7, 9, 6], True
)
fio = student_list[0]
vozrast = (CURRENT_YEAR - student_list[1])
otsenki = student_list[2]
print ("Фамилия, Имя Студента:", fio)
print ("Оценки", otsenki)
print ('Средняя оценка',statistics.mean(otsenki))
print ('конец задания')
if sum(otsenki) > 7:
    print ("Повышенная стипендия: есть")
else:
    print ("Повышенная стипендия:нет")
print ('конец задания')

