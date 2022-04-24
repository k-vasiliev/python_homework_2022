"""
В папке data лежат файлы
Ваша задача создать zip архив, в котором будут лежать только изображения из этой папки

Определять является ли файл изображением нужно по расширению
Найти информацию по работе с zip в python вам нужно самостоятельно

"""
import os
import zipfile

FOLDER = 'data'
file_extension_all = ['jpeg', 'png', 'gif', 'bmp', 'pds', 'wmf']
files_to_add_in_zip = []

create_zip = zipfile.ZipFile('zip_test.zip', 'w')


def zip_images():
    for filename in os.listdir(FOLDER):
        file_extension = filename[filename.find('.') + 1:len(filename)]
        if file_extension in file_extension_all:
            files_to_add_in_zip.append(filename)
    return files_to_add_in_zip


zip_images()
for file in files_to_add_in_zip:
    name = os.path.join(FOLDER, file)
    create_zip.write(name)
create_zip.close()

z = zipfile.ZipFile('zip_test.zip', 'r')
z.printdir()  # просмотр содержимого
