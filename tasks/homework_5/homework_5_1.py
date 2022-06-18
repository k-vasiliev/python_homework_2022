"""
В папке data лежат файлы
Ваша задача создать zip архив, в котором будут лежать только изображения из этой папки

Определять является ли файл изображением нужно по расширению
Найти информацию по работе с zip в python вам нужно самостоятельно

"""
import os
import zipfile

images_extensions = (".bmp", ".jpg", ".jpeg", ".png", ".tiff", ".gif", ".wmf")


def zip_images(folder):
    #получаем список файлов в папке
    files_list = os.listdir(folder)

    # создаём архив
    z = zipfile.ZipFile('images.zip', 'w')

    # проходим по файлам в папке, если расширение подходит, то добавляем в архив
    for file in files_list:
        if file.endswith(images_extensions):
            z.write(os.path.join(folder, file))
    z.close()
    z.printdir()


zip_images('data')
