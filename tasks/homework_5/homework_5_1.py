"""
В папке data лежат файлы
Ваша задача создать zip архив, в котором будут лежать только изображения из этой папки

Определять является ли файл изображением нужно по расширению
Найти информацию по работе с zip в python вам нужно самостоятельно

"""


def zip_images():
    import os
    import zipfile

    images_format = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif", ".wmf") # список всех изображений

    file_path = 'data'
    file_names = os.listdir(file_path)

    z = zipfile.ZipFile('image_files.zip', 'w')        # Создание нового архива
    for root, dirs, files in os.walk('data'):          # Список всех файлов и папок в директории data
        for file in files:
            if os.path.splitext(file)[1] in images_format:
                z.write(os.path.join(root,file))
    z.close()


zip_images()

