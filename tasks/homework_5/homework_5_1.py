"""
В папке data лежат файлы
Ваша задача создать zip архив, в котором будут лежать только изображения из этой папки

Определять является ли файл изображением нужно по расширению
Найти информацию по работе с zip в python вам нужно самостоятельно

"""
import shutil, glob

def zip_images(source: str, destination: str):
    """  pass

 source = "C:\\Users\julia\Documents\Питон_ВШЭ\img_source"
  destination = "C:\\Users\julia\Documents\Питон_ВШЭ\img_destin" """

    for file in glob.glob(source+"\*.jpg"):
        shutil.copy2(file, destination);

    shutil.make_archive(destination, 'zip', destination)
    return print('ready')

zip_images("C:\\Users\julia\Documents\Питон_ВШЭ\img_source", "C:\\Users\julia\Documents\Питон_ВШЭ\img_destin")
"""

"""