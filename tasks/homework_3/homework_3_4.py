"""
Дан список из словарей
Напишите программу, которая объединяет значения в один словарь
Структура всегда одна и та же - товар и количество

Ввод:
shops = [
    {'товар': 'яблоки', 'количество': 400},
    {'товар': 'конфеты', 'количество': 300},
    {'товар': 'яблоки', 'количество': 750}
]
Вывод:
{'яблоки': 1150, 'конфеты': 300}
"""

shops = [
    {'товар': 'яблоки', 'количество': 400},
    {'товар': 'конфеты', 'количество': 300},
    {'товар': 'яблоки', 'количество': 750}
]

resultdict = {}

kol_vo = 0
new_k = 0
tovar = ''
for i in shops:
    if i['товар'] in resultdict:
        for j in resultdict:
            if j == i['товар']:
                new_k = resultdict[j]
        new_k = new_k + i['количество']
        resultdict[i['товар']] = new_k
    else:
        tovar = i['товар']
        kol_vo = i['количество']
        resultdict[tovar] = kol_vo
print(resultdict)









#for i in shops:
#    for key in i.keys():
#        print(key)
#        try:

#            resultdict[i[key]] += i[key]
#        except KeyError:
#            resultdict[i[key]] = i[key]
#print(resultdict)



#for element in shops:
#    for key in element.keys():
#            n = element[key]
#            new_d.append(n)

#print(new_d)




#while shops != '':



#        try:
#            if j in new_dict2:
#                new_dict2[j] = new_dict[j]
#            else:
#                new_dict2[j] = new_dict[j] + new_dict2[j]
#        except KeyError:
#            new_dict2[j] = new_dict[j]


