"""
В папке data лежат файлы
Ваша задача создать zip архив, в котором будут лежать только изображения из этой папки

Определять является ли файл изображением нужно по расширению
Найти информацию по работе с zip в python вам нужно самостоятельно

"""
import os
import zipfile
import re

folder_name = 'data'


def zip_images(folder):
    list_of_files = os.listdir(folder)

    list_of_images = []
    for i in list_of_files:
        if re.search(r'\.jpeg|\.png', i) is not None:
            list_of_images.append(i)

    zip_object = zipfile.ZipFile('images.zip', 'w')
    for i in list_of_images:
        zip_object.write(fr'{folder}\{i}')
    zip_object.close()


zip_images(folder_name)
