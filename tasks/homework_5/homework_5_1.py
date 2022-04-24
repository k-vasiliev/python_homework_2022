"""
В папке data лежат файлы
Ваша задача создать zip архив, в котором будут лежать только изображения из этой папки

Определять является ли файл изображением нужно по расширению
Найти информацию по работе с zip в python вам нужно самостоятельно

"""


"""
В папке data лежат файлы
Ваша задача создать zip архив, в котором будут лежать только изображения из этой папки

Определять является ли файл изображением нужно по расширению
Найти информацию по работе с zip в python вам нужно самостоятельно

"""

import os
from zipfile import ZipFile
from os import path

def zip_images():
    images_format = {'jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif',
                  'tiff'}
    for i in os.listdir('data'):
        if i.split('.')[-1] in images_format:
            srs_path = path.join('data',i)
            src = path.realpath(srs_path)
            root_dir,tail = path.split(src)
            with ZipFile("archive_images.zip", "a") as newzip:
                newzip.write(srs_path)

