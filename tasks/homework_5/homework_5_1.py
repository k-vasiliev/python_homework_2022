"""
В папке data лежат файлы
Ваша задача создать zip архив, в котором будут лежать только изображения из этой папки
Определять является ли файл изображением нужно по расширению
Найти информацию по работе с zip в python вам нужно самостоятельно
###
"""

import zipfile, os, fnmatch

"""
path = 'data'
suffix_file = r'.png', r'.jpeg'

for item in os.listdir(path):
    print('TRUE =>', item) \
    if item.endswith(suffix_file) \
    else print('NO =>', item)
"""
# Можно написать через рекурсию обход?
path = 'data'
listOfFiles = os.listdir(path)
pattern_1 = "*.png"
pattern_2 = "*.jpeg"

with zipfile.ZipFile('HW5_1.zip', mode='w', \
                     compression=zipfile.ZIP_DEFLATED) as zf:
    for file in listOfFiles:
        if fnmatch.fnmatch(file, pattern_1):
            add_file = os.path.join(path, file)
            zf.write(add_file)
        if fnmatch.fnmatch(file, pattern_2):
            add_file = os.path.join(path, file)
            zf.write(add_file)
print('Файлы с изображением добавлены в архив!')