#Логика следующая. Сравниваем высоту с другой переменной, пока размер меньше высоты-
# мы увеличиваем высоту через добавления элемента в множество в цикле. Пока размер строки меньше введеного числа, продолжаем его увеличивать.
#с помощью функции join, которая работает только со строчными переменными
# Команда возвращает строку, созданную путем соединения элементов итерации с помощью разделителя строк.
# map здесь для последовательной итерации каждой переменной в строчную. 'пробел' для их разделения
#
N = int(input('введите число для построения лесенки высотой до этого числа'))
height = 0  # задаем переменную, в которую будем вставлять высоту лесенки
size = 0 # переменная, с которой сравниваем высоту лесенки, и которая выступает ограничителем
new_list = list() # множество, где мы храним высоту
while size < N: # запускаем цикл
    height += 1
    new_list.append(height)
    print(' '.join(map(str, new_list))) #объединяет каждый элемент итерируемого объекта (например, список, строку и кортеж) с помощью разделителя строк и возвращает объединенную строку. Источник: https://pythonstart.ru/string/join-python
    size += 1 # если не прописать увеличение этой переменной, то итерация будет идти до бесконечности по всем осям. здесь мы поставим стоп.