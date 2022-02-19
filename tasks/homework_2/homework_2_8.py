# Используя список dwarves, выведите на экран с помощью срезов следующие списки:

# ["Двалин", "Бифур", "Бофур"]
# ["Балин", "Бифур", "Бомбур", "Глоин", "Нори", "Фили", "Торин"]
# ["Оин", "Дори", "Ори", "Кили"]
# ["Торин", "Фили", "Нори", "Глоин"]
dwarves = ["Балин", "Двалин", "Бифур", "Бофур",
         "Бомбур", "Оин", "Глоин", "Дори", "Нори",
         "Ори", "Фили", "Кили", "Торин"]

dwarves1 = dwarves[1:4]
print(dwarves1)

dwarves2 = dwarves[0::2]
print(dwarves2)

index_oin = dwarves.index("Оин")
dwarves3 = dwarves[index_oin::2]
print(dwarves3)

dwarves_reverse = dwarves[::-1]
index_gloin = dwarves_reverse.index("Глоин")
dwarves4 = dwarves_reverse[0:index_gloin+1:2]
print(dwarves4)