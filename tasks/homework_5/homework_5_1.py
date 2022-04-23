"""
В папке data лежат файлы
Ваша задача создать zip архив, в котором будут лежать только изображения из этой папки

Определять является ли файл изображением нужно по расширению
Найти информацию по работе с zip в python вам нужно самостоятельно

"""
import os
import zipfile


def zip_images(folder):
# создадим кортеж из списка возможных расширений и найдем все файлы с данными расширениями
    images_extensions = (".png", ".jpeg", ".tiff", ".gif", ".jpg", ".bmp", ".wmf")
# создадим архив
    z = zipfile.ZipFile('images.zip', 'w')
# ищем все файлы-изображения и добавляем в архив
    for file in os.listdir(folder):
        if file.endswith(images_extensions):
            print(os.path.join(file))
            z.write(os.path.join(folder, file))
    z.close()

zip_images(".\data")



