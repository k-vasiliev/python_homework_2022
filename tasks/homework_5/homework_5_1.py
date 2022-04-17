"""
В папке data лежат файлы
Ваша задача создать zip архив, в котором будут лежать только изображения из этой папки

Определять является ли файл изображением нужно по расширению
Найти информацию по работе с zip в python вам нужно самостоятельно C:\\Users\\79031\\PycharmProjects\\python_homework_2022\\tasks\\homework_5\\data

"""

#даем возможность при вызове хотя бы задать назвать свой архив, при этом задав дефолтное значние
def zip_images(archive_name: str = 'img_archive', path_name: str = 'C:\\Users\\79031\\PycharmProjects\\python_homework_2022\\tasks\\homework_5\\data\\'):
    # вытаскиваем библиотеки, принципиально делаем это в функции
    import os
    import zipfile

    # cоздадим список расширений изображений
    list_of_img_ext = ('.png', '.jpg', '.jpeg', '.bmp')

    # поменяем рабочий каталог
    os.chdir(path_name)

    #создадим архив и воткнем в него нужные файлы
    with zipfile.ZipFile(archive_name + '.zip', 'w') as new_zip:
        for file in os.listdir():
            if os.path.splitext(file)[1] in list_of_img_ext:
                new_zip.write(file)

    return

zip_images()
