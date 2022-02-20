# Используя список dwarves, выведите на экран с помощью срезов следующие списки:

# ["Двалин", "Бифур", "Бофур"]
# ["Балин", "Бифур", "Бомбур", "Глоин", "Нори", "Фили", "Торин"]
# ["Оин", "Дори", "Ори", "Кили"]
# ["Торин", "Фили", "Нори", "Глоин"]
dwarves = ["Балин", "Двалин", "Бифур", "Бофур",
           "Бомбур", "Оин", "Глоин", "Дори", "Нори",
           "Ори", "Фили", "Кили", "Торин"]

pattern_1 = ["Двалин", "Бифур", "Бофур"]
my_list_1 = []
for i in pattern_1:
    for k in dwarves:
        if i == k:
            my_list_1.append(k)

pattern_2 = ["Балин", "Бифур", "Бомбур", "Глоин", "Нори", "Фили", "Торин"]
my_list_2 = []

for i in pattern_2:
    for k in dwarves:
        if i == k:
            my_list_2.append(k)

pattern_3 = ["Оин", "Дори", "Ори", "Кили"]
my_list_3 = []

for i in pattern_3:
    for k in dwarves:
        if i == k:
            my_list_3.append(k)

pattern_4 = ["Торин", "Фили", "Нори", "Глоин"]
my_list_4 = []

for i in pattern_4:
    for k in dwarves:
        if i == k:
            my_list_4.append(k)

print(my_list_1, my_list_2, my_list_3, my_list_4, sep='\n')
