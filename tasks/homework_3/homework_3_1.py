
polzovat_stroka = input('введите что-нибудь')
text_string = polzovat_stroka.split() #разделяем ввод на элементы
unikal_slova = set(text_string) # решаем через множества, поскольку множества уникальны
for words in unikal_slova: # запускаем for для проверки количества уникальных слов
    print('Частота использования слова:', words, 'is :', text_string.count(words))



