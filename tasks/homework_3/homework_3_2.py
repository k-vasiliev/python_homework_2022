polzovat_stroka = input('введите что-нибудь')
hranilishe = { 'Буквы': 0, 'Цифры': 0} # создаем множество
for i in polzovat_stroka: # это у нас генератор
    if i.isalpha(): # проверяем, состоит ли строка из буквы
        hranilishe['Буквы'] += 1
    elif i.isdigit():
        hranilishe['Цифры'] += 1 #Метод isdigit() проверяет состоит ли строка из цифр
print(('цифры:'),hranilishe['Цифры'],('буквы:'),hranilishe['Буквы'])
