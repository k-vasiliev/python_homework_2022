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
#Нет пересечений
#{'английский', 'сольфеджио', 'право'}
#{'математика', 'сольфеджио'}
#{'немецкий', 'право'}

Vasya = input('Факультативы Васи: ')
Petya = input('Факультативы Пети: ')
Misha = input('Факультативы Миши: ')

Vasya = set(Vasya.split(' '))
Petya = set(Petya.split(' '))
Misha = set(Misha.split(' '))

if Vasya.intersection(Petya, Misha):
    print('2')
else:
    print('0')




