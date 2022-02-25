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
"""
#игнорируем регистр на случай если в заявках он будет разный
student_1_disciplines = input('Первый студент: ').lower()
student_2_disciplines = input('Второй студент: ').lower()
student_3_disciplines = input('Третий студент: ').lower()

#примем за константу кол-во студентов
number_of_students = 3

#соединим заявки воедино, убрав возможные дубли в списке заявок каждого студента, дополнительно создадим набор уникальных факультативов в заявке
total_list = list(set(student_1_disciplines.split(' '))) + list(set(student_2_disciplines.split(' '))) + list(set(student_3_disciplines.split(' ')))
total_set = set(total_list)

#создаем пустой список
check_list = list()

#начинаем цикл до опустошения множества
while len(total_set) != 0:
    #вытаскиваем элемент из множества
    temp_value = total_set.pop()
    #считаем кол-во его вхождений в список заявок
    counter = total_list.count(temp_value)
    #если кол-во заявок равно кол-ву студентов, то вставляем название предмета в список для проверки
    if counter == number_of_students:
        check_list.append(temp_value)

print(len(check_list))
"""

#студенты вводят заявки через пробел, превращаем их заявки в множества, предварительно вырованяв регистр
#разделим строки с помощью разделителя пробелом
student_1_disciplines = set(input('Первый студент: ').lower().split(' '))
student_2_disciplines = set(input('Второй студент: ').lower().split(' '))
student_3_disciplines = set(input('Третий студент: ').lower().split(' '))

#удалим пустоты на случай, если студент поставил пробел более одного раза
student_1_disciplines.discard('')
student_2_disciplines.discard('')
student_3_disciplines.discard('')

#обрабатываем пересечения
intersection = student_1_disciplines & student_2_disciplines & student_3_disciplines

#выводим результат
print(len(intersection))
