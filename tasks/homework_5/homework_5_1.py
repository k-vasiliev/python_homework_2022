"""
В папке data лежат файлы
Ваша задача создать zip архив, в котором будут лежать только изображения из этой папки

Определять является ли файл изображением нужно по расширению
Найти информацию по работе с zip в python вам нужно самостоятельно

"""
import os
from zipfile import ZipFile
from os import path
import shutil


def zip_images():
    pass


# создать zip-архив, в котором будут лежать изображения
# найти информацию по работе с zip файлами

fileExt = r".jpeg", r".png"

source_path = [os.path.join("data", i) for i in os.listdir("data") if i.endswith(fileExt)]
print(source_path)

for i in source_path:
    if path.exists(i):
        destination_path = "archive_images.zip"
        new_location = shutil.move(i, destination_path)
        with ZipFile("archive_images.zip", "a") as newzip:
            newzip.write(new_location)

















