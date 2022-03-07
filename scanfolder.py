import os
import shutil

FILES_INPUT = 'C:/Users/admin/Desktop/python/rookie' # Входные файлы
FILES_OUTPUT = 'C:/Users/admin/Desktop/python/' # Выходные файлы

for filename in os.listdir(FILES_INPUT):
     filepath = os.path.join(FILES_INPUT, filename) #Путь и файл
     base, ext = os.path.splitext(filepath) # Создаем папку назначения
     os.mkdir(base) # Создаем папку как название файла
     path = shutil.move(filepath, base) # Перенесем файл внутрь папки
     print(path)
