"""
В папке data лежат файлы
Ваша задача создать zip архив, в котором будут лежать только изображения из этой папки

Определять является ли файл изображением нужно по расширению
Найти информацию по работе с zip в python вам нужно самостоятельно

"""

def zip_images():
    pass

import os
import zipfile

zip_images = zipfile.ZipFile('zip_images.zip', 'w', zipfile.ZIP_DEFLATED)

for folder, subfolders, files in os.walk('C://example//images'):
    for file in files:
        if file.endswith('.jpg'):
            zip_images.write(os.path.join (folder, file), os.path.relpath (os.path.join(folder, file), 'C://example//images'))
zip_images.close()