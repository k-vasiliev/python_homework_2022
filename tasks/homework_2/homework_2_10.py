print ('Задание № 10')
student_1_disciplines = {"английский","сольфеджио","право"}
student_2_disciplines ={"математика","сольфеджио","немецкий"}
student_3_disciplines = {'английский','немецкий'}
a = student_1_disciplines.intersection(student_2_disciplines)
b = (student_2_disciplines.intersection(student_3_disciplines ))
c = (student_3_disciplines.intersection(student_1_disciplines))
print ('Дисциплины студента №1:',a,b,c)
print ('Дисциплины студента №2:',a,b,c)
print ('Дисциплины студента №1:',b,c)
print ('конец задания')
