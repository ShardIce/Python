import os
import shutil

FILES_INPUT = 'C:/Users/admin/Desktop/python/rookie' # Входные файлы
FILES_OUTPUT = 'C:/Users/admin/Desktop/python/' # Выходные файлы

dirpath = FILES_INPUT #Путь к файлам
for filename in os.listdir(dirpath):
     filepath = os.path.join(dirpath, filename) #Путь и файл
     dirpath, filename = os.path.split(filepath) #Путь, файлы
     base, ext = os.path.splitext(filepath)
     source = filepath
     destination = base
     # Создаем папку назначения
     os.mkdir(destination)
     # Перенесем файл внутрь папки
     path = shutil.move(source, destination)
     print(path)
