"""
В папке data лежат файлы
Ваша задача создать zip архив, в котором будут лежать только изображения из этой папки

Определять является ли файл изображением нужно по расширению
Найти информацию по работе с zip в python вам нужно самостоятельно

"""
import os
import zipfile

def zip_images(folder):
    images_extensions = (".png", ".tiff", ".tif", ".gif", ".jpeg", ".jpg", ".jp2", ".bmp", ".dib", ".wmf")
    zip_file = zipfile.ZipFile('images.zip', 'w')
    for file in os.listdir(folder):
        if file.endswith(images_extensions):
            print(os.path.join(file))
            zip_file.write(os.path.join(folder, file))
    zip_file.close()

zip_images(".\data")