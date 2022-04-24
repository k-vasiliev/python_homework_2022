"""
В папке data лежат файлы
Ваша задача создать zip архив, в котором будут лежать только изображения из этой папки

Определять является ли файл изображением нужно по расширению
Найти информацию по работе с zip в python вам нужно самостоятельно
"""

import os
import zipfile

def zip_images():
    os.chdir('/Users/nikaborisova/PycharmProjects/python_homework_2022/tasks/homework_5/data')
    files_list = os.listdir()
    formats = ('.png', '.jpeg')
    images_zip = zipfile.ZipFile('images.zip', 'w')

    for file in files_list:
        if file.endswith(formats):
            images_zip.write(file)

    images_zip.close()
    return images_zip.printdir()

zip_images()
