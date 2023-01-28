import os
import shutil

FILES_INPUT = 'C:/Users/admin/Desktop/python/rookie'
FILES_OUTPUT = 'C:/Users/admin/Desktop/python/rookie'

for filename in os.listdir(FILES_INPUT):
    filepath = os.path.join(FILES_INPUT, filename)
    if os.path.isfile(filepath): # Проверяем файл или папка
     base, ext = os.path.splitext(filepath) # Создаем папку назначения
     os.makedirs(base, exist_ok=True) # Создаем папку как название файла
     path = shutil.move(filepath, base) # Перенесем файл внутрь папки
     print(path)
    else:
     print('Это папка:', filename)
