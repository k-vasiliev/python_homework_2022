
# Задание_2
# пользователь вводит две строки (по очереди)
input1 = input("1-ая фраза: ")
input1 = input1.lower()
input2 = input("2-ая фраза: ")
input2 = input2.lower()
if input1 == input2:
    print("пусто")
# Считайте ввод и распечатайте первую фразу с места, где заканчивается вторая
# строка 2 содержится в строке 1?
if input2 in input1:
    len2 = len(input2)
    print("вывод: ", input1[len2:])





